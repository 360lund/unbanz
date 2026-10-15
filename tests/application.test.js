import test from 'node:test';
import assert from 'node:assert/strict';
import handler from '../api/application.js';

async function invoke(body, method = 'POST', headers = {}) {
  const res = {
    code: 0,
    setHeader() {},
    status(n) {
      this.code = n;
      return this;
    },
    json(data) {
      this.data = data;
      return this;
    }
  };
  await handler(
    {
      method,
      headers: {
        'content-type': 'application/json',
        host: 'unbanz.com',
        origin: 'https://unbanz.com',
        ...headers
      },
      body
    },
    res
  );
  return res;
}

test('validation, provider errors and successful fixed-recipient delivery', async () => {
  delete process.env.RESEND_API_KEY;
  delete process.env.APPLICATION_FROM;
  assert.equal((await invoke(null, 'GET')).data.ready, false);
  assert.equal((await invoke({})).code, 503);
  process.env.RESEND_API_KEY = 'test-only';
  process.env.APPLICATION_FROM = 'Unbanz <applications@unbanz.com>';
  let calls = 0;
  global.fetch = async (url, opts) => {
    calls++;
    const b = JSON.parse(opts.body);
    assert.deepEqual(b.to, ['team@unbanz.com']);
    assert.equal(b.reply_to, 'customer@example.com');
    assert.ok(opts.headers['Idempotency-Key']);
    return { ok: true, json: async () => ({ id: 'mock-id' }) };
  };
  const valid = {
    service: 'Instagram unban',
    account: '@example',
    email: 'customer@example.com',
    details: 'Suspended',
    company: ''
  };
  assert.equal((await invoke({ ...valid, email: 'bad\r\nemail' })).code, 400);
  assert.equal((await invoke({ ...valid, service: 'not-listed' })).code, 400);
  assert.equal((await invoke({ ...valid, company: 'bot' })).code, 400);
  assert.equal((await invoke(valid, 'POST', { origin: 'https://other.test' })).code, 403);
  assert.equal(calls, 0);
  assert.equal((await invoke(valid)).data.accepted, true);
  assert.equal(calls, 1);
  global.fetch = async () => ({ ok: false, json: async () => ({ error: 'provider failed' }) });
  assert.equal((await invoke(valid)).code, 502);
  global.fetch = async () => {
    throw new Error('network');
  };
  assert.equal((await invoke(valid)).code, 502);
});
