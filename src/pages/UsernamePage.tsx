import React from 'react';
import { PageView } from '../types';
import {
  UserCheck,
  ArrowUpRight,
  CheckCircle2,
  AlertCircle,
  Shield,
  Award,
  Sparkles,
  HelpCircle,
  MessageCircle
} from 'lucide-react';

interface UsernamePageProps {
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const UsernamePage: React.FC<UsernamePageProps> = ({ onNavigate }) => {
  return (
    <div className="space-y-16 pb-20">
      {/* Hero Header */}
      <section className="bg-gradient-to-b from-[#eaf4fb] to-[#f5f9fc] border-b border-[#e2edf6] py-14 md:py-20">
        <div className="max-w-5xl mx-auto px-4 sm:px-6">
          <div className="max-w-3xl">
            <span className="text-xs font-bold uppercase tracking-wider text-[#2c5b85] bg-white border border-[#cbe1f2] px-3.5 py-1.5 rounded-full inline-block mb-4 shadow-2xs">
              Brand Identity Acquisition
            </span>
            <h1 className="text-4xl sm:text-5xl font-extrabold text-[#18334a] tracking-tight leading-[1.15] mb-6">
              Instagram username claims & brand acquisition.
            </h1>
            <p className="text-base sm:text-lg text-[#4a6b87] leading-relaxed mb-8">
              Claim dormant, inactive, or trademark-infringing Instagram usernames. Secure the exact digital identity for your brand, executive profile, or enterprise without public handle snipers.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <button
                onClick={() => onNavigate('apply', { service: 'Instagram username claim' })}
                className="inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-xs sm:text-sm font-semibold shadow-md transition-all cursor-pointer"
              >
                <span>Check Username Feasibility</span>
                <ArrowUpRight className="w-4 h-4 text-[#7cb7ea]" />
              </button>
              <a
                href="https://wa.me/19342012490"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-5 py-3.5 rounded-full bg-white hover:bg-[#f0f6fa] text-[#2c567a] text-xs sm:text-sm font-semibold border border-[#cde0f0] transition-colors"
              >
                <MessageCircle className="w-4 h-4 text-[#25D366]" />
                WhatsApp Advisory
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Criteria & Rules */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-4">
              <Award className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Trademark Claims</h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              If your business owns a registered trademark (USPTO, EUIPO, or national IP office) matching the handle, we lodge direct intellectual property priority claims.
            </p>
          </div>

          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-4">
              <UserCheck className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Dormant Handles</h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              Target handles must show proven inactivity (no recent posts, dormant engagement, or abandoned registration). Handles must typically be 6+ characters unless trademark-supported.
            </p>
          </div>

          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#eaf4fb] text-[#3b7bb5] flex items-center justify-center mb-4">
              <Shield className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Safe Handle Swap</h3>
            <p className="text-xs text-[#527390] leading-relaxed">
              Never risk losing a handle during a rename. We facilitate direct profile swap protocols so automated bots and snipers cannot hijack the released username.
            </p>
          </div>
        </div>
      </section>

      {/* Case Requirements */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="bg-[#18334a] text-white rounded-3xl p-8 sm:p-10">
          <span className="text-xs font-bold uppercase tracking-wider text-[#7cb7ea] bg-white/10 px-3 py-1 rounded-full inline-block mb-3">
            Eligibility Checklist
          </span>
          <h2 className="text-2xl sm:text-3xl font-bold mb-4">
            Requirements for Instagram username claims
          </h2>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mt-6 text-xs text-[#cde2f2]">
            <div className="bg-white/5 p-4 rounded-xl border border-white/10 flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-[#7cb7ea] shrink-0 mt-0.5" />
              <div>
                <strong className="block text-white mb-0.5">Desired Username (@handle)</strong>
                The exact username requested and the URL of the current holder account.
              </div>
            </div>

            <div className="bg-white/5 p-4 rounded-xl border border-white/10 flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-[#7cb7ea] shrink-0 mt-0.5" />
              <div>
                <strong className="block text-white mb-0.5">Target Destination Profile</strong>
                Your existing active Instagram account that will receive the claimed username.
              </div>
            </div>

            <div className="bg-white/5 p-4 rounded-xl border border-white/10 flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-[#7cb7ea] shrink-0 mt-0.5" />
              <div>
                <strong className="block text-white mb-0.5">Brand / Trademark Proof</strong>
                Trademark registration, articles of incorporation, or business website matching the name.
              </div>
            </div>

            <div className="bg-white/5 p-4 rounded-xl border border-white/10 flex items-start gap-3">
              <CheckCircle2 className="w-5 h-5 text-[#7cb7ea] shrink-0 mt-0.5" />
              <div>
                <strong className="block text-white mb-0.5">Clean Policy Record</strong>
                Destination profile must have no active policy strikes or pending restrictions.
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* What we do not do */}
      <section className="max-w-3xl mx-auto px-4 text-center">
        <div className="inline-flex items-center gap-2 text-xs font-semibold text-[#8a531e] bg-[#fdf5eb] border border-[#f5dfc3] px-3.5 py-1.5 rounded-full mb-4">
          <AlertCircle className="w-4 h-4 text-[#d97706]" />
          Policy Compliance Guarantee
        </div>
        <h3 className="text-xl font-bold text-[#18334a] mb-2">
          Strict adherence to official policy
        </h3>
        <p className="text-xs text-[#527390] leading-relaxed mb-6">
          We strictly do not engage in unauthorized SIM swapping, extortion, unauthorized handle takeover, or cracking active personal profiles. All claims are processed via registered trademark priority and inactive policy compliance.
        </p>
        <button
          onClick={() => onNavigate('apply', { service: 'Instagram username claim' })}
          className="px-6 py-3 rounded-full bg-[#599fe0] hover:bg-[#458ecc] text-white text-xs font-bold shadow-sm transition-all cursor-pointer"
        >
          Submit Username Claim Case ↗
        </button>
      </section>
    </div>
  );
};
