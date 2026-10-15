import React from 'react';
import { PageView } from '../types';
import {
  AlertOctagon,
  ArrowUpRight,
  CheckCircle2,
  ShieldCheck,
  FileWarning,
  EyeOff,
  Scale,
  MessageCircle
} from 'lucide-react';

interface BanPageProps {
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const BanPage: React.FC<BanPageProps> = ({ onNavigate }) => {
  return (
    <div className="space-y-16 pb-20">
      {/* Hero Header */}
      <section className="bg-gradient-to-b from-[#fdf4f4] via-[#faf7f7] to-[#f5f9fc] border-b border-[#ebdcdc] py-14 md:py-20">
        <div className="max-w-5xl mx-auto px-4 sm:px-6">
          <div className="max-w-3xl">
            <span className="text-xs font-bold uppercase tracking-wider text-[#9d3838] bg-white border border-[#f0c8c8] px-3.5 py-1.5 rounded-full inline-block mb-4 shadow-2xs">
              Trust & Safety Enforcement
            </span>
            <h1 className="text-4xl sm:text-5xl font-extrabold text-[#18334a] tracking-tight leading-[1.15] mb-6">
              Ban requests & impersonation takedowns.
            </h1>
            <p className="text-base sm:text-lg text-[#556e84] leading-relaxed mb-8">
              Enforce Meta Community Standards against malicious impersonators, counterfeit storefronts, and severe intellectual property infringements that standard report buttons fail to resolve.
            </p>
            <div className="flex flex-wrap items-center gap-4">
              <button
                onClick={() => onNavigate('apply', { service: 'Ban request — genuine policy violation' })}
                className="inline-flex items-center gap-2.5 px-6 py-3.5 rounded-full bg-[#9d3838] hover:bg-[#852f2f] text-white text-xs sm:text-sm font-semibold shadow-md transition-all cursor-pointer"
              >
                <span>Report Severe Violation</span>
                <ArrowUpRight className="w-4 h-4 text-[#fca5a5]" />
              </button>
              <a
                href="https://wa.me/19342012490"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 px-5 py-3.5 rounded-full bg-white hover:bg-[#fbf3f3] text-[#7d3232] text-xs sm:text-sm font-semibold border border-[#e8cece] transition-colors"
              >
                <MessageCircle className="w-4 h-4 text-[#25D366]" />
                Urgent WhatsApp Escalation
              </a>
            </div>
          </div>
        </div>
      </section>

      {/* Categories of Legitimate Ban Requests */}
      <section className="max-w-5xl mx-auto px-4 sm:px-6">
        <div className="text-center max-w-2xl mx-auto mb-12">
          <h2 className="text-2xl sm:text-3xl font-extrabold text-[#18334a]">
            Qualifying Policy Violations
          </h2>
          <p className="text-xs sm:text-sm text-[#527390] mt-2">
            We only escalate requests backed by substantiated evidence of genuine policy breaches under Meta terms.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#fdf2f2] text-[#c04b4b] flex items-center justify-center mb-4">
              <EyeOff className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Executive & Brand Impersonation</h3>
            <p className="text-xs text-[#527390] leading-relaxed mb-4">
              Fraudulent profiles using your likeness, brand photos, or company name to defraud followers, run crypto investment scams, or phish customers.
            </p>
            <ul className="space-y-1.5 text-xs text-[#375a77]">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Exact-match avatar & bio cloning
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Scam DMs to genuine customer base
              </li>
            </ul>
          </div>

          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#fdf2f2] text-[#c04b4b] flex items-center justify-center mb-4">
              <Scale className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Counterfeit & Trademark Abuse</h3>
            <p className="text-xs text-[#527390] leading-relaxed mb-4">
              Accounts illegally utilizing trademarked brand assets, selling counterfeit goods, or misrepresenting official affiliation without license.
            </p>
            <ul className="space-y-1.5 text-xs text-[#375a77]">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Counterfeit e-commerce storefronts
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Unauthorized trademark commercialization
              </li>
            </ul>
          </div>

          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#fdf2f2] text-[#c04b4b] flex items-center justify-center mb-4">
              <FileWarning className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Systematic Copyright Theft</h3>
            <p className="text-xs text-[#527390] leading-relaxed mb-4">
              Rogue channels systematically re-uploading proprietary photography, videos, and artistic assets after standard DMCA reports fail or get contested.
            </p>
            <ul className="space-y-1.5 text-xs text-[#375a77]">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Repeat infringer policy triggering
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Permanent profile termination
              </li>
            </ul>
          </div>

          <div className="bg-white p-7 rounded-2xl border border-[#dce9f4] shadow-xs">
            <div className="w-10 h-10 rounded-xl bg-[#fdf2f2] text-[#c04b4b] flex items-center justify-center mb-4">
              <AlertOctagon className="w-5 h-5" />
            </div>
            <h3 className="text-lg font-bold text-[#18334a] mb-2">Targeted Harassment & Defamation</h3>
            <p className="text-xs text-[#527390] leading-relaxed mb-4">
              Coordinated smear campaigns, hate speech, or non-consensual personal information disclosure (doxxing) violating Meta community policies.
            </p>
            <ul className="space-y-1.5 text-xs text-[#375a77]">
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Doxxing & private data exposure
              </li>
              <li className="flex items-center gap-2">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#599fe0]" />
                Coordinated harassment networks
              </li>
            </ul>
          </div>
        </div>
      </section>

      {/* Ethical Boundary Notice */}
      <section className="max-w-4xl mx-auto px-4 sm:px-6">
        <div className="bg-[#18334a] text-white rounded-3xl p-8 sm:p-10 border border-[#224461]">
          <div className="flex items-center gap-3 mb-4">
            <ShieldCheck className="w-6 h-6 text-[#7cb7ea]" />
            <h3 className="text-xl font-bold">Policy & Ethics Statement</h3>
          </div>
          <p className="text-xs sm:text-sm text-[#a2c4de] leading-relaxed mb-6">
            Unbanz will <strong>never</strong> accept payment to weaponize false reports against competitors, innocent individuals, or accounts that do not violate genuine Meta policies. All requests undergo an internal legal audit prior to escalation.
          </p>
          <button
            onClick={() => onNavigate('apply', { service: 'Ban request — genuine policy violation' })}
            className="px-6 py-3 rounded-full bg-[#599fe0] hover:bg-[#458ecc] text-white text-xs font-bold transition-all cursor-pointer"
          >
            Submit Policy Evidence Dossier ↗
          </button>
        </div>
      </section>
    </div>
  );
};
