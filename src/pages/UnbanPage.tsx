import React from 'react';
import { PageView } from '../types';
import {
  ShieldAlert,
  ArrowUpRight,
  CheckCircle2,
  AlertTriangle,
  Clock,
  Sparkles,
  HelpCircle,
  FileText,
  MessageCircle
} from 'lucide-react';

interface UnbanPageProps {
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const UnbanPage: React.FC<UnbanPageProps> = ({ onNavigate }) => {
  return (
    <div className="space-y-16 pb-20">
      {/* Hero Header */}
      <section className="bg-gradient-to-b from-[#eaf4fb] to-[#f5f9fc] border-b border-[#e2edf6] py-14 md:py-20">
        <div className="max-w-5xl mx-auto px-4 sm:px-6">
          <div className="max-w-3xl">
            <span className="text-xs font-bold uppercase tracking-wider text-[#2c5b85] bg-white border border-[#cbe1f2] px-3.5 py-1.5 rounded-full inline-block mb-4 shadow-2xs">
              Recovery & Appeals
            </span>
            <h1 className="text-4xl sm:text-5xl font-extrabold text-[#18334a] tracking-tight leading-[1.15] mb-6">
              Instagram and Facebook account unbans.
            </h1>
            <p className="text-base sm:text-lg text-[#4a6b87] leading-relaxed mb-8">
              Banned or disabled? Personal profiles, creator accounts, verified badges, and Meta Business ad accounts. Send your account for an internal case feasibility review.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <button
                onClick={() => onNavigate('apply', { service: 'Instagram unban' })}
                className="inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-xs sm:text-sm font-semibold shadow-md transition-all cursor-pointer"
              >
                <span>Submit Account for Review</span>
                <ArrowUpRight className="w-4 h-4 text-[#7cb7ea]" />
              </button>
              <a
                href="https://wa.me/19342012490"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-5 py-3.5 rounded-full bg-white hover:bg-[#f0f6fa] text-[#2c567a] text-xs sm:text-sm font-semibold border border-[#cde0f0] transition-colors"
              >
                <MessageCircle className="w-4 h-4 text-[#25D366]" />
                WhatsApp Consultation
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Main Breakdown Grid */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
          {/* Instagram Unbans */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center font-bold">
                IG
              </div>
              <div>
                <h3 className="text-xl font-bold text-[#18334a]">Instagram Unbans</h3>
                <p className="text-xs text-[#527390]">Personal, Creator & Business</p>
              </div>
            </div>
            <p className="text-xs text-[#527390] leading-relaxed mb-5">
              Instagram's automated moderation algorithms regularly trigger false positive bans, locking users out without an effective way to appeal. We handle:
            </p>
            <ul className="space-y-2.5 text-xs text-[#375a77] mb-6">
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Community Guidelines bans:</strong> Alleged hate speech, spam, or nudity false-positives.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Terms of Use bans:</strong> Commercial use, third-party follower tools, API flags.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Integrity & Artificial Activity:</strong> Automated security blocks after rapid follower growth or logging in abroad.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Permanently Disabled Status:</strong> Cases where the in-app appeal button disappeared or says "Decision is final".</span>
              </li>
            </ul>
            <button
              onClick={() => onNavigate('apply', { service: 'Instagram unban' })}
              className="w-full py-2.5 rounded-xl bg-[#f0f6fc] hover:bg-[#e4eff8] text-[#18334a] text-xs font-bold transition-colors cursor-pointer text-center"
            >
              Start Instagram Case Review ↗
            </button>
          </div>

          {/* Facebook & Ad Accounts */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs">
            <div className="flex items-center gap-3 mb-4">
              <div className="w-10 h-10 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center font-bold">
                FB
              </div>
              <div>
                <h3 className="text-xl font-bold text-[#18334a]">Facebook & Ad Accounts</h3>
                <p className="text-xs text-[#527390]">Profiles, Pages & Meta Business Manager</p>
              </div>
            </div>
            <p className="text-xs text-[#527390] leading-relaxed mb-5">
              A banned Facebook profile halts business operations, ad spending, and client page management. We escalate:
            </p>
            <ul className="space-y-2.5 text-xs text-[#375a77] mb-6">
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Disabled Facebook Profiles:</strong> Name verification blocks, 180-day countdown locks.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Meta Business Manager:</strong> Restricted business accounts blocking ad delivery.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Ad Account Reinstatement:</strong> Policy reviews for e-commerce, crypto, or health brands.</span>
              </li>
              <li className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-[#599fe0] shrink-0 mt-0.5" />
                <span><strong>Page Admin Recovery:</strong> Reclaiming lost administrative rights to corporate Pages.</span>
              </li>
            </ul>
            <button
              onClick={() => onNavigate('apply', { service: 'Facebook unban' })}
              className="w-full py-2.5 rounded-xl bg-[#f0f6fc] hover:bg-[#e4eff8] text-[#18334a] text-xs font-bold transition-colors cursor-pointer text-center"
            >
              Start Facebook Case Review ↗
            </button>
          </div>
        </div>
      </section>

      {/* Checklist / Requirements */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="bg-[#18334a] text-white rounded-3xl p-8 sm:p-10">
          <div className="max-w-3xl">
            <span className="text-xs font-bold uppercase tracking-wider text-[#7cb7ea] bg-white/10 px-3 py-1 rounded-full inline-block mb-3">
              Case Preparation
            </span>
            <h2 className="text-2xl sm:text-3xl font-bold mb-4">
              What we need to review your ban
            </h2>
            <p className="text-xs sm:text-sm text-[#a2c4de] leading-relaxed mb-8">
              To expedite internal review, please gather the following information before submitting your application.
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-[#cde2f2]">
              <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                <strong className="block text-white mb-1 font-semibold">1. Account Identifier</strong>
                Exact @handle, linked email address, and original phone number.
              </div>
              <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                <strong className="block text-white mb-1 font-semibold">2. Restriction Notice</strong>
                Screenshot of the exact ban screen (e.g. "We suspended your account" or "Account disabled").
              </div>
              <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                <strong className="block text-white mb-1 font-semibold">3. Timeline & Preceding Events</strong>
                Date the restriction started and any password changes, logins abroad, or campaign launches.
              </div>
              <div className="bg-white/5 p-4 rounded-xl border border-white/10">
                <strong className="block text-white mb-1 font-semibold">4. Identity Verification</strong>
                Government ID or corporate registration (only if requested during official escalation).
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Case submission bottom CTA */}
      <section className="text-center max-w-2xl mx-auto px-4">
        <h3 className="text-2xl font-bold text-[#18334a] mb-3">
          Have an urgent disabled account?
        </h3>
        <p className="text-xs sm:text-sm text-[#527390] mb-6">
          Every day an account remains disabled increases the latency of the internal review pipeline. Submit your handle today for immediate case logging.
        </p>
        <button
          onClick={() => onNavigate('apply', { service: 'Instagram & Facebook unbans' })}
          className="px-8 py-3.5 rounded-full bg-[#599fe0] hover:bg-[#458ecc] text-white text-xs sm:text-sm font-bold shadow-md transition-all cursor-pointer"
        >
          Open Case Review Form ↗
        </button>
      </section>
    </div>
  );
};
