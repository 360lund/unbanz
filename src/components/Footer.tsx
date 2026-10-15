import React from 'react';
import { PageView } from '../types';
import { ArrowUpRight, MessageCircle, Mail } from 'lucide-react';

interface FooterProps {
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigate }) => {
  return (
    <footer className="bg-[#18334a] text-[#a4bed3] border-t border-[#224461] pt-16 pb-12">
      <div className="max-w-6xl mx-auto px-4 sm:px-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-10 pb-12 border-b border-[#244866]">
          {/* Brand info */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-xl bg-[#599fe0] flex items-center justify-center text-white font-bold text-lg shadow-sm">
                u.
              </div>
              <span className="text-2xl font-bold tracking-tight text-white">
                unbanz<span className="text-[#599fe0]">.</span>
              </span>
            </div>
            <p className="text-sm text-[#8faec7] max-w-md leading-relaxed">
              Instagram and Facebook account recovery, ad account unbans, genuine policy violation enforcement, and inactive username claims. Direct case review with specialist attention.
            </p>
            <div className="flex items-center gap-3 pt-2">
              <a
                href="https://wa.me/19342012490"
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-2 text-xs font-medium text-white bg-[#224968] hover:bg-[#2b577b] px-3.5 py-2 rounded-lg transition-colors border border-[#305b82]"
              >
                <MessageCircle className="w-3.5 h-3.5 text-[#25D366]" />
                +1 (934) 201-2490
              </a>
              <a
                href="mailto:team@unbanz.com"
                className="inline-flex items-center gap-2 text-xs font-medium text-[#c0d8ea] hover:text-white bg-[#224968] hover:bg-[#2b577b] px-3.5 py-2 rounded-lg transition-colors border border-[#305b82]"
              >
                <Mail className="w-3.5 h-3.5 text-[#599fe0]" />
                team@unbanz.com
              </a>
            </div>
          </div>

          {/* Services Links */}
          <div>
            <h4 className="text-xs font-bold tracking-wider uppercase text-white mb-4">
              Services
            </h4>
            <ul className="space-y-2.5 text-xs">
              <li>
                <button
                  onClick={() => onNavigate('unban')}
                  className="hover:text-white transition-colors cursor-pointer"
                >
                  Instagram Account Unbans
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('unban')}
                  className="hover:text-white transition-colors cursor-pointer"
                >
                  Facebook Profile Unbans
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('apply', { service: 'Ad account unban' })}
                  className="hover:text-white transition-colors cursor-pointer"
                >
                  Meta Business Ad Accounts
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('username')}
                  className="hover:text-white transition-colors cursor-pointer"
                >
                  Instagram Username Claims
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('ban')}
                  className="hover:text-white transition-colors cursor-pointer"
                >
                  Impersonation & Ban Requests
                </button>
              </li>
            </ul>
          </div>

          {/* Quick links & internal portal */}
          <div>
            <h4 className="text-xs font-bold tracking-wider uppercase text-white mb-4">
              Client Portal
            </h4>
            <ul className="space-y-2.5 text-xs">
              <li>
                <button
                  onClick={() => onNavigate('apply')}
                  className="inline-flex items-center gap-1 text-white hover:text-[#7cb7ea] transition-colors cursor-pointer"
                >
                  <span>Submit Case Review</span>
                  <ArrowUpRight className="w-3 h-3" />
                </button>
              </li>
              <li>
                <button
                  onClick={() => onNavigate('admin')}
                  className="inline-flex items-center gap-1 text-[#8faec7] hover:text-white transition-colors cursor-pointer"
                >
                  <span>Lead Desk Demo</span>
                </button>
              </li>
              <li>
                <span className="text-[#64849f]">
                  No upfront charge on infeasible cases
                </span>
              </li>
              <li>
                <span className="text-[#64849f]">
                  Strict NDAs & Client Confidentiality
                </span>
              </li>
            </ul>
          </div>
        </div>

        {/* Disclaimer */}
        <div className="pt-8 flex flex-col md:flex-row items-center justify-between gap-4 text-[11px] text-[#698da7]">
          <p>
            © {new Date().getFullYear()} Unbanz. All rights reserved. Unbanz is an independent case review and escalation consultancy. Meta, Instagram, and Facebook are trademarks of Meta Platforms, Inc.
          </p>
          <div className="flex items-center gap-4">
            <span>Confidential Review</span>
            <span>·</span>
            <span>Direct Escalation</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
