import React from 'react';
import { PageView } from '../types';
import {
  ShieldAlert,
  UserCheck,
  Briefcase,
  AlertOctagon,
  ArrowRight,
  ArrowUpRight,
  CheckCircle2,
  Lock,
  Clock,
  Sparkles,
  MessageCircle,
  HelpCircle
} from 'lucide-react';

interface HomePageProps {
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const HomePage: React.FC<HomePageProps> = ({ onNavigate }) => {
  return (
    <div className="space-y-20 pb-20">
      {/* Hero Section */}
      <section className="relative overflow-hidden pt-12 md:pt-20 pb-16 md:pb-24 border-b border-[#e2edf6] bg-gradient-to-b from-[#eaf4fb] via-[#f5f9fc] to-[#f5f9fc]">
        {/* Subtle decorative sky backdrop */}
        <div className="absolute top-0 left-1/2 -translate-x-1/2 w-[1000px] h-[350px] bg-gradient-to-r from-[#d3e8f8]/60 via-[#b9ddf8]/40 to-[#e2effa]/50 rounded-full blur-3xl -z-10 pointer-events-none" />

        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="max-w-3xl">
            <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white border border-[#cbe1f2] text-[#2c5b85] text-xs font-semibold uppercase tracking-wider mb-6 shadow-2xs">
              <span className="w-2 h-2 rounded-full bg-[#599fe0] animate-pulse" />
              Instagram & Facebook Escalation Desk
            </div>

            <h1 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-[#18334a] tracking-tight leading-[1.12] mb-6">
              The fast track back to your{' '}
              <span className="text-[#367ebf] underline decoration-[#a5d2f8] decoration-4 underline-offset-4">
                Instagram & Facebook
              </span>
              .
            </h1>

            <p className="text-lg md:text-xl text-[#4a6b87] leading-relaxed mb-8 max-w-2xl font-normal">
              Account recovery for disabled or banned profiles, Meta Business ad account unbans, and inactive Instagram username claims. Direct case review with specialized escalation.
            </p>

            <div className="flex flex-wrap items-center gap-4">
              <button
                onClick={() => onNavigate('apply')}
                className="inline-flex items-center gap-3 px-6 py-3.5 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-sm font-semibold shadow-md hover:shadow-lg transition-all group cursor-pointer"
              >
                <span>Submit Case Review</span>
                <ArrowUpRight className="w-4 h-4 text-[#7cb7ea] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
              </button>

              <button
                onClick={() => onNavigate('unban')}
                className="inline-flex items-center gap-2 px-5 py-3.5 rounded-full bg-white hover:bg-[#f0f6fa] text-[#2c567a] text-sm font-semibold border border-[#cde0f0] transition-colors cursor-pointer shadow-2xs"
              >
                <span>Explore Unban Services</span>
                <ArrowRight className="w-4 h-4 text-[#599fe0]" />
              </button>

              <a
                href="https://wa.me/19342012490"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-4 py-3.5 rounded-full text-[#1c6742] hover:bg-[#eaf8f0] text-sm font-medium transition-colors"
              >
                <MessageCircle className="w-4 h-4 text-[#25D366]" />
                WhatsApp Quick Chat
              </a>
            </div>

            {/* Quick trust metrics */}
            <div className="grid grid-cols-3 gap-6 pt-10 mt-10 border-t border-[#d8e8f4]">
              <div>
                <p className="text-2xl sm:text-3xl font-bold text-[#18334a]">24–72h</p>
                <p className="text-xs text-[#60809b] mt-0.5 font-medium">Average Review Speed</p>
              </div>
              <div>
                <p className="text-2xl sm:text-3xl font-bold text-[#18334a]">$0 Upfront</p>
                <p className="text-xs text-[#60809b] mt-0.5 font-medium">Free Case Evaluation</p>
              </div>
              <div>
                <p className="text-2xl sm:text-3xl font-bold text-[#18334a]">100%</p>
                <p className="text-xs text-[#60809b] mt-0.5 font-medium">Strict Confidentiality</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Core Services Grid */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="text-center max-w-2xl mx-auto mb-14">
          <p className="text-xs font-bold text-[#599fe0] uppercase tracking-widest mb-2">
            Specialized Practice Areas
          </p>
          <h2 className="text-3xl md:text-4xl font-extrabold text-[#18334a] tracking-tight">
            How we help creators, brands & agencies
          </h2>
          <p className="text-sm md:text-base text-[#527390] mt-3">
            Every case is handled through direct policy compliance workflows and representative appeals, avoiding broken automated form loops.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {/* Card 1: Instagram & Facebook Unbans */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <div className="w-12 h-12 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-5 group-hover:scale-105 transition-transform">
                <ShieldAlert className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#599fe0] bg-[#f0f7fc] px-2.5 py-1 rounded-md">
                Most Requested
              </span>
              <h3 className="text-xl font-bold text-[#18334a] mt-3 mb-2">
                Instagram & Facebook Unbans
              </h3>
              <p className="text-xs text-[#527390] leading-relaxed mb-6">
                Restoration for accounts disabled for Terms of Service, Community Guidelines, alleged impersonation, artificial activity, or sudden AI false-flag bans.
              </p>
              <ul className="space-y-2 text-xs text-[#375a77] mb-6">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Personal and creator profile unbans
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Permanent disabled status appeals
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Hacked & compromised profile recovery
                </li>
              </ul>
            </div>
            <button
              onClick={() => onNavigate('unban')}
              className="inline-flex items-center justify-between w-full pt-4 border-t border-[#edf4fa] text-xs font-semibold text-[#18334a] group-hover:text-[#377cb7] cursor-pointer"
            >
              <span>Learn about unban procedures</span>
              <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </button>
          </div>

          {/* Card 2: Ad Accounts & Business Manager */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <div className="w-12 h-12 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-5 group-hover:scale-105 transition-transform">
                <Briefcase className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#4787bf] bg-[#f0f7fc] px-2.5 py-1 rounded-md">
                E-Commerce & Agencies
              </span>
              <h3 className="text-xl font-bold text-[#18334a] mt-3 mb-2">
                Meta Ad Account Recovery
              </h3>
              <p className="text-xs text-[#527390] leading-relaxed mb-6">
                Unblocking disabled Meta Business Managers, restricted ad accounts, rejected payment methods, and lost Page ownership rights.
              </p>
              <ul className="space-y-2 text-xs text-[#375a77] mb-6">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  BM & Ad account restrictions lifting
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Page Admin & Ownership escalations
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Advertising policy audit & reinstatement
                </li>
              </ul>
            </div>
            <button
              onClick={() => onNavigate('apply', { service: 'Ad account unban' })}
              className="inline-flex items-center justify-between w-full pt-4 border-t border-[#edf4fa] text-xs font-semibold text-[#18334a] group-hover:text-[#377cb7] cursor-pointer"
            >
              <span>Submit ad account case</span>
              <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </button>
          </div>

          {/* Card 3: Instagram Username Claims */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <div className="w-12 h-12 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-5 group-hover:scale-105 transition-transform">
                <UserCheck className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#4787bf] bg-[#f0f7fc] px-2.5 py-1 rounded-md">
                Brand Identity
              </span>
              <h3 className="text-xl font-bold text-[#18334a] mt-3 mb-2">
                Instagram Username Claims
              </h3>
              <p className="text-xs text-[#527390] leading-relaxed mb-6">
                Acquire dormant, inactive, or trademark-infringing Instagram usernames directly through brand verification and trademark claims.
              </p>
              <ul className="space-y-2 text-xs text-[#375a77] mb-6">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Claim inactive handles (6+ letters or verified)
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Registered trademark alignment
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Safe transfer directly to target profile
                </li>
              </ul>
            </div>
            <button
              onClick={() => onNavigate('username')}
              className="inline-flex items-center justify-between w-full pt-4 border-t border-[#edf4fa] text-xs font-semibold text-[#18334a] group-hover:text-[#377cb7] cursor-pointer"
            >
              <span>Explore username claim requirements</span>
              <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </button>
          </div>

          {/* Card 4: Ban Requests / Impersonation */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <div className="w-12 h-12 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-5 group-hover:scale-105 transition-transform">
                <AlertOctagon className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#c04b4b] bg-[#fdf2f2] px-2.5 py-1 rounded-md">
                Enforcement
              </span>
              <h3 className="text-xl font-bold text-[#18334a] mt-3 mb-2">
                Ban Requests & Impersonation
              </h3>
              <p className="text-xs text-[#527390] leading-relaxed mb-6">
                Take down impersonators, malicious clone accounts, and perpetrators of severe copyright/trademark infringements under official policy.
              </p>
              <ul className="space-y-2 text-xs text-[#375a77] mb-6">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Executive & brand impersonator removal
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Counterfeit store & scam account takedown
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Targeted policy violations enforcement
                </li>
              </ul>
            </div>
            <button
              onClick={() => onNavigate('ban')}
              className="inline-flex items-center justify-between w-full pt-4 border-t border-[#edf4fa] text-xs font-semibold text-[#18334a] group-hover:text-[#377cb7] cursor-pointer"
            >
              <span>View policy ban requirements</span>
              <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </button>
          </div>

          {/* Card 5: Hacked Account Recovery */}
          <div className="bg-white rounded-2xl p-7 border border-[#dce9f4] shadow-xs hover:shadow-md transition-all flex flex-col justify-between group">
            <div>
              <div className="w-12 h-12 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-5 group-hover:scale-105 transition-transform">
                <Lock className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#4787bf] bg-[#f0f7fc] px-2.5 py-1 rounded-md">
                Security Urgent
              </span>
              <h3 className="text-xl font-bold text-[#18334a] mt-3 mb-2">
                Hacked & Hijacked Recovery
              </h3>
              <p className="text-xs text-[#527390] leading-relaxed mb-6">
                When email, phone number, and 2FA are replaced by attackers. We assist in reclaiming access back to original verified owners.
              </p>
              <ul className="space-y-2 text-xs text-[#375a77] mb-6">
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Bypass altered 2-factor authentication
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Origin email & identity re-anchoring
                </li>
                <li className="flex items-center gap-2">
                  <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0] shrink-0" />
                  Security lockdown against re-breach
                </li>
              </ul>
            </div>
            <button
              onClick={() => onNavigate('apply', { service: 'Hacked account recovery' })}
              className="inline-flex items-center justify-between w-full pt-4 border-t border-[#edf4fa] text-xs font-semibold text-[#18334a] group-hover:text-[#377cb7] cursor-pointer"
            >
              <span>Submit hijacked profile case</span>
              <ArrowRight className="w-4 h-4 transition-transform group-hover:translate-x-1" />
            </button>
          </div>

          {/* Card 6: Direct Case Review Callout */}
          <div className="bg-gradient-to-br from-[#18334a] to-[#254b6d] text-white rounded-2xl p-7 shadow-sm flex flex-col justify-between">
            <div>
              <div className="w-12 h-12 rounded-xl bg-white/10 text-[#7cb7ea] flex items-center justify-center mb-5">
                <Sparkles className="w-6 h-6" />
              </div>
              <span className="text-[11px] font-bold tracking-wider uppercase text-[#9cc9ee] bg-white/10 px-2.5 py-1 rounded-md">
                Fast Turnaround
              </span>
              <h3 className="text-xl font-bold text-white mt-3 mb-2">
                Unsure which category your issue falls into?
              </h3>
              <p className="text-xs text-[#b3cfe4] leading-relaxed mb-6">
                Send your handle and a screenshot of the restriction notice. Our escalation analysts will assess the reason code and provide a clear recovery plan.
              </p>
            </div>
            <button
              onClick={() => onNavigate('apply', { service: 'Something else' })}
              className="inline-flex items-center justify-center gap-2 w-full py-3 px-4 rounded-xl bg-[#599fe0] hover:bg-[#458ecc] text-white text-xs font-bold transition-all shadow-sm cursor-pointer"
            >
              <span>Request Free Case Evaluation</span>
              <ArrowUpRight className="w-4 h-4" />
            </button>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="bg-white border-y border-[#e2edf6] py-16">
        <div className="max-w-6xl mx-auto px-4 sm:px-6">
          <div className="text-center max-w-2xl mx-auto mb-14">
            <p className="text-xs font-bold text-[#599fe0] uppercase tracking-widest mb-2">
              Transparent Methodology
            </p>
            <h2 className="text-3xl font-extrabold text-[#18334a]">
              How the Unbanz process works
            </h2>
            <p className="text-xs sm:text-sm text-[#527390] mt-3">
              We never ask for your password. We utilize direct internal documentation appeals and compliance channels.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="relative p-6 rounded-2xl bg-[#f8fbfe] border border-[#e2ecf5]">
              <div className="w-10 h-10 rounded-full bg-[#18334a] text-white font-bold flex items-center justify-center text-sm mb-4">
                1
              </div>
              <h3 className="text-lg font-bold text-[#18334a] mb-2">Submit Case Details</h3>
              <p className="text-xs text-[#527390] leading-relaxed">
                Provide the target @handle, the initial notification screenshot, and the date the restriction was applied. No passwords needed.
              </p>
            </div>

            <div className="relative p-6 rounded-2xl bg-[#f8fbfe] border border-[#e2ecf5]">
              <div className="w-10 h-10 rounded-full bg-[#599fe0] text-white font-bold flex items-center justify-center text-sm mb-4">
                2
              </div>
              <h3 className="text-lg font-bold text-[#18334a] mb-2">Feasibility & Strategy</h3>
              <p className="text-xs text-[#527390] leading-relaxed">
                Our team audits the policy violation reason code. If your case is deemed non-viable, we inform you honestly with no fee.
              </p>
            </div>

            <div className="relative p-6 rounded-2xl bg-[#f8fbfe] border border-[#e2ecf5]">
              <div className="w-10 h-10 rounded-full bg-[#204360] text-white font-bold flex items-center justify-center text-sm mb-4">
                3
              </div>
              <h3 className="text-lg font-bold text-[#18334a] mb-2">Direct Escalation</h3>
              <p className="text-xs text-[#527390] leading-relaxed">
                We lodge the authorized case dossier with dedicated Meta internal review channels. You receive real-time updates until recovery.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Frequently Asked Questions */}
      <section className="max-w-4xl mx-auto px-4 sm:px-6">
        <div className="text-center mb-12">
          <p className="text-xs font-bold text-[#599fe0] uppercase tracking-widest mb-2">
            Frequently Answered
          </p>
          <h2 className="text-3xl font-extrabold text-[#18334a]">
            Common questions about bans and unbans
          </h2>
        </div>

        <div className="space-y-4">
          <div className="bg-white p-6 rounded-2xl border border-[#dce8f2]">
            <h3 className="text-base font-bold text-[#18334a] mb-2 flex items-center gap-2">
              <HelpCircle className="w-4 h-4 text-[#599fe0]" />
              Do you need my account password?
            </h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              Never. We do not require or ask for your password. All submissions are conducted via official representative channels and identity verification proofs.
            </p>
          </div>

          <div className="bg-white p-6 rounded-2xl border border-[#dce8f2]">
            <h3 className="text-base font-bold text-[#18334a] mb-2 flex items-center gap-2">
              <Clock className="w-4 h-4 text-[#599fe0]" />
              How long does an Instagram or Facebook unban typically take?
            </h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              Most standard review cases conclude within 24 to 72 hours once submitted to the specialist escalation queue. Complex cases involving multi-layer policy violations can take 5 to 7 business days.
            </p>
          </div>

          <div className="bg-white p-6 rounded-2xl border border-[#dce8f2]">
            <h3 className="text-base font-bold text-[#18334a] mb-2 flex items-center gap-2">
              <Lock className="w-4 h-4 text-[#599fe0]" />
              What if my account was permanently disabled with no appeal button?
            </h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              When the in-app appeal button is removed or grayed out, standard customer forms will loop indefinitely. Our escalation dossiers bypass the broken form flow through authorized compliance channels.
            </p>
          </div>
        </div>
      </section>

      {/* Bottom CTA Banner */}
      <section className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="bg-[#18334a] rounded-3xl p-8 sm:p-12 text-white relative overflow-hidden flex flex-col md:flex-row items-center justify-between gap-8">
          <div className="relative z-10 max-w-xl">
            <span className="text-xs font-bold uppercase tracking-wider text-[#7cb7ea] bg-white/10 px-3 py-1 rounded-full">
              Let's resolve this today
            </span>
            <h3 className="text-2xl sm:text-3xl font-extrabold text-white mt-4 mb-3">
              Ready to recover your account or claim your brand name?
            </h3>
            <p className="text-xs sm:text-sm text-[#a2c4de] leading-relaxed">
              Submit your handle for a free case assessment. A specialist will review your case within hours.
            </p>
          </div>

          <div className="relative z-10 flex flex-col sm:flex-row gap-3 w-full md:w-auto">
            <button
              onClick={() => onNavigate('apply')}
              className="px-6 py-3.5 rounded-full bg-[#599fe0] hover:bg-[#458ecc] text-white text-xs sm:text-sm font-bold shadow-md transition-all text-center cursor-pointer whitespace-nowrap"
            >
              Start Case Review ↗
            </button>
            <a
              href="https://wa.me/19342012490"
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-3.5 rounded-full bg-white/10 hover:bg-white/20 text-white text-xs sm:text-sm font-semibold transition-all text-center whitespace-nowrap"
            >
              WhatsApp Us
            </a>
          </div>
        </div>
      </section>
    </div>
  );
};
