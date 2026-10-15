import React, { useState, useEffect } from 'react';
import { PageView, ServiceType } from '../types';
import {
  ArrowRight,
  CheckCircle2,
  AlertCircle,
  Clock,
  ShieldCheck,
  MessageCircle,
  HelpCircle,
  Send,
  Loader2
} from 'lucide-react';

interface ApplyPageProps {
  initialService?: string;
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

const serviceOptions: ServiceType[] = [
  'Instagram unban',
  'Facebook unban',
  'Instagram & Facebook unbans',
  'Ad account unban',
  'Hacked account recovery',
  'Instagram username claim',
  'Ban request — genuine policy violation',
  'Page access & ownership',
  'Impersonation & content reports',
  'Profile & name changes',
  'Something else'
];

export const ApplyPage: React.FC<ApplyPageProps> = ({ initialService, onNavigate }) => {
  const [service, setService] = useState<ServiceType>('Instagram unban');
  const [account, setAccount] = useState('');
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [details, setDetails] = useState('');
  const [company, setCompany] = useState(''); // Honeypot
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [errorMessage, setErrorMessage] = useState('');
  const [submittedLeadId, setSubmittedLeadId] = useState<number | null>(null);
  const [isSimulated, setIsSimulated] = useState(false);

  useEffect(() => {
    if (initialService && serviceOptions.includes(initialService as ServiceType)) {
      setService(initialService as ServiceType);
    }
  }, [initialService]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrorMessage('');

    // Client validation
    if (!account.trim() || account.trim().length < 2) {
      setErrorMessage('Please provide a valid account @handle or account ID.');
      return;
    }
    if (!email.trim() || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setErrorMessage('Please enter a valid email address for case communications.');
      return;
    }
    if (details.length > 1200) {
      setErrorMessage('Case details must be under 1,200 characters.');
      return;
    }

    setIsSubmitting(true);

    try {
      const res = await fetch('/api/application', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          service,
          account: account.trim(),
          email: email.trim(),
          name: name.trim(),
          phone: phone.trim(),
          details: details.trim(),
          company // honeypot
        })
      });

      const data = await res.json();

      if (!res.ok) {
        setErrorMessage(data.error || 'Failed to submit application. Please check your inputs.');
        setIsSubmitting(false);
        return;
      }

      setSubmittedLeadId(data.leadId || Math.floor(1000 + Math.random() * 9000));
      setIsSimulated(Boolean(data.simulated));
      setIsSubmitting(false);
    } catch {
      setErrorMessage('Network error while submitting. You can also contact us directly on WhatsApp.');
      setIsSubmitting(false);
    }
  };

  const handleResetForm = () => {
    setSubmittedLeadId(null);
    setAccount('');
    setEmail('');
    setName('');
    setPhone('');
    setDetails('');
    setErrorMessage('');
  };

  if (submittedLeadId !== null) {
    return (
      <div className="max-w-2xl mx-auto px-4 py-16 text-center">
        <div className="bg-white rounded-3xl p-8 sm:p-12 border border-[#dce8f2] shadow-sm">
          <div className="w-16 h-16 rounded-full bg-[#e8f7ee] text-[#1c6742] flex items-center justify-center mx-auto mb-6">
            <CheckCircle2 className="w-9 h-9" />
          </div>

          <span className="text-xs font-bold tracking-wider uppercase text-[#1c6742] bg-[#eaf5ef] px-3 py-1 rounded-full inline-block mb-3">
            Case Dossier Received
          </span>

          <h2 className="text-3xl font-extrabold text-[#18334a] mb-2">
            Application submitted successfully
          </h2>

          <p className="text-sm text-[#527390] mb-6">
            Case Reference Number:{' '}
            <span className="font-mono font-bold text-[#18334a] bg-[#f0f6fc] px-2.5 py-1 rounded-md border border-[#d2e2f0]">
              #UBZ-{submittedLeadId}
            </span>
          </p>

          <div className="bg-[#f8fbfe] rounded-2xl p-6 text-left border border-[#e2edf6] mb-8 space-y-3 text-xs text-[#3b5e7d]">
            <div className="flex justify-between border-b border-[#eaf1f7] pb-2">
              <span className="text-[#6c8ba4]">Service Requested:</span>
              <strong className="text-[#18334a]">{service}</strong>
            </div>
            <div className="flex justify-between border-b border-[#eaf1f7] pb-2">
              <span className="text-[#6c8ba4]">Target Account:</span>
              <strong className="text-[#18334a]">{account}</strong>
            </div>
            <div className="flex justify-between border-b border-[#eaf1f7] pb-2">
              <span className="text-[#6c8ba4]">Contact Email:</span>
              <strong className="text-[#18334a]">{email}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#6c8ba4]">Next Step:</span>
              <span className="text-[#2c6591] font-semibold">Specialist review within 2–6 hours</span>
            </div>
          </div>

          {isSimulated && (
            <div className="p-4 rounded-xl bg-[#eaf3fb] text-[#2c5b85] text-xs text-left mb-6 border border-[#cde0f0]">
              <strong className="block mb-1">Demo / In-App Lead Desk Integration:</strong>
              This application has been recorded in the live demo lead database! You can view and manage it immediately in the{' '}
              <button
                onClick={() => onNavigate('admin')}
                className="underline font-bold hover:text-[#18334a] cursor-pointer"
              >
                Lead Desk
              </button>
              .
            </div>
          )}

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
            <button
              onClick={handleResetForm}
              className="w-full sm:w-auto px-6 py-3 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-xs font-semibold transition-colors cursor-pointer"
            >
              Submit Another Case
            </button>
            <button
              onClick={() => onNavigate('admin')}
              className="w-full sm:w-auto px-6 py-3 rounded-full bg-white hover:bg-[#f0f6fa] text-[#2c567a] text-xs font-semibold border border-[#cde0f0] transition-colors cursor-pointer"
            >
              View in Lead Desk ↗
            </button>
            <a
              href={`https://wa.me/19342012490?text=${encodeURIComponent(`Hi Unbanz team, I submitted case #UBZ-${submittedLeadId} for ${account}.`)}`}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-6 py-3 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white text-xs font-bold transition-colors"
            >
              <MessageCircle className="w-4 h-4" />
              Follow up on WhatsApp
            </a>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 py-12 md:py-16 space-y-12">
      <div className="text-center max-w-2xl mx-auto">
        <span className="text-xs font-bold uppercase tracking-wider text-[#2c5b85] bg-white border border-[#cbe1f2] px-3.5 py-1.5 rounded-full inline-block mb-3 shadow-2xs">
          Direct Case Review
        </span>
        <h1 className="text-3xl sm:text-4xl font-extrabold text-[#18334a] tracking-tight">
          Send your account for case review.
        </h1>
        <p className="text-xs sm:text-sm text-[#527390] mt-3 leading-relaxed">
          Fill in the details below. Our team reviews policy history and account status to confirm feasibility before any work begins.
        </p>
      </div>

      <div className="bg-white rounded-3xl p-6 sm:p-10 border border-[#dce8f2] shadow-xs">
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* Honeypot anti-bot field */}
          <div className="hidden">
            <label htmlFor="company">Company</label>
            <input
              id="company"
              type="text"
              value={company}
              onChange={(e) => setCompany(e.target.value)}
              tabIndex={-1}
              autoComplete="off"
            />
          </div>

          {/* Service Selector */}
          <div>
            <label className="block text-xs font-bold uppercase tracking-wider text-[#355776] mb-2">
              Select Practice Area / Service *
            </label>
            <select
              value={service}
              onChange={(e) => setService(e.target.value as ServiceType)}
              className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all"
            >
              {serviceOptions.map((opt) => (
                <option key={opt} value={opt}>
                  {opt}
                </option>
              ))}
            </select>
          </div>

          {/* Account handle input */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="block text-xs font-bold uppercase tracking-wider text-[#355776]">
                Target Account / Handle / ID *
              </label>
              <span className="text-[11px] text-[#698ba7]">e.g. @yourhandle or Business ID</span>
            </div>
            <div className="relative">
              <input
                type="text"
                required
                placeholder="@username or ad account ID"
                value={account}
                onChange={(e) => setAccount(e.target.value)}
                maxLength={240}
                className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all font-mono"
              />
            </div>
          </div>

          {/* Contact Details (Email + Name + Phone) */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#355776] mb-2">
                Your Reply Email *
              </label>
              <input
                type="email"
                required
                placeholder="you@domain.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                maxLength={254}
                className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#355776] mb-2">
                Your Name (Optional)
              </label>
              <input
                type="text"
                placeholder="Full Name / Brand Rep"
                value={name}
                onChange={(e) => setName(e.target.value)}
                maxLength={100}
                className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all"
              />
            </div>
          </div>

          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="block text-xs font-bold uppercase tracking-wider text-[#355776]">
                WhatsApp / Phone Number (Optional)
              </label>
              <span className="text-[11px] text-[#698ba7]">For fast messaging updates</span>
            </div>
            <input
              type="tel"
              placeholder="+1 (555) 000-0000"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
              maxLength={30}
              className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all"
            />
          </div>

          {/* Details / What happened */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <label className="block text-xs font-bold uppercase tracking-wider text-[#355776]">
                Case Details & Background
              </label>
              <span className="text-[11px] text-[#698ba7]">
                {details.length}/1200 characters
              </span>
            </div>
            <textarea
              rows={4}
              placeholder="Describe what occurred: exact error text, date the restriction began, whether appeals were attempted, and any trademark numbers..."
              value={details}
              onChange={(e) => setDetails(e.target.value)}
              maxLength={1200}
              className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl p-4 focus:outline-none focus:ring-2 focus:ring-[#599fe0] focus:border-transparent transition-all resize-y"
            />
          </div>

          {/* Error display */}
          {errorMessage && (
            <div className="p-4 rounded-xl bg-[#fdf2f2] border border-[#f5c6c6] text-[#9e3a3a] text-xs flex items-center gap-2.5">
              <AlertCircle className="w-4 h-4 shrink-0" />
              <span>{errorMessage}</span>
            </div>
          )}

          {/* Submit Button */}
          <div className="pt-2">
            <button
              type="submit"
              disabled={isSubmitting}
              className="w-full inline-flex items-center justify-center gap-2 py-4 px-6 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-sm font-bold shadow-md hover:shadow-lg transition-all disabled:opacity-50 cursor-pointer"
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin text-[#7cb7ea]" />
                  <span>Submitting case dossier...</span>
                </>
              ) : (
                <>
                  <span>Submit Case for Review</span>
                  <ArrowRight className="w-4 h-4 text-[#7cb7ea]" />
                </>
              )}
            </button>
          </div>

          {/* Guarantees */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-6 border-t border-[#edf4fa] text-[11px] text-[#61839e]">
            <div className="flex items-center gap-1.5">
              <ShieldCheck className="w-4 h-4 text-[#599fe0] shrink-0" />
              <span>No password ever required</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Clock className="w-4 h-4 text-[#599fe0] shrink-0" />
              <span>Response in 24–72 hours</span>
            </div>
            <div className="flex items-center gap-1.5">
              <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0" />
              <span>Free initial evaluation</span>
            </div>
          </div>
        </form>
      </div>

      {/* Alternative WhatsApp chat */}
      <div className="bg-[#f2f8fc] rounded-2xl p-6 border border-[#d6e7f4] flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>
          <h4 className="text-sm font-bold text-[#18334a]">
            Prefer direct messaging?
          </h4>
          <p className="text-xs text-[#527390] mt-0.5">
            You can message our case intake team directly on WhatsApp for immediate priority queries.
          </p>
        </div>
        <a
          href="https://wa.me/19342012490"
          target="_blank"
          rel="noopener noreferrer"
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-[#25D366] hover:bg-[#20ba59] text-white text-xs font-bold shadow-2xs transition-colors shrink-0"
        >
          <MessageCircle className="w-4 h-4" />
          Chat on WhatsApp
        </a>
      </div>
    </div>
  );
};
