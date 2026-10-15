import React from 'react';
import { PageView } from '../types';
import { ArrowUpRight, MessageCircle, ShieldCheck } from 'lucide-react';

interface HeaderProps {
  currentPage: PageView;
  onNavigate: (page: PageView, searchParams?: { service?: string }) => void;
}

export const Header: React.FC<HeaderProps> = ({ currentPage, onNavigate }) => {
  return (
    <header className="sticky top-0 z-50 bg-[#f5f9fc]/90 backdrop-blur-md border-b border-[#e2ecf5]">
      <div className="max-w-6xl mx-auto px-4 sm:px-6 h-20 flex items-center justify-between">
        {/* Brand */}
        <button
          onClick={() => onNavigate('home')}
          className="flex items-center gap-2.5 text-left group cursor-pointer focus:outline-none"
        >
          <div className="w-8 h-8 rounded-xl bg-[#599fe0] flex items-center justify-center text-white font-bold text-lg shadow-sm group-hover:bg-[#478ecc] transition-colors">
            u.
          </div>
          <span className="text-2xl font-bold tracking-tight text-[#18334a]">
            unbanz<span className="text-[#599fe0]">.</span>
          </span>
        </button>

        {/* Navigation */}
        <nav className="hidden md:flex items-center gap-1.5 bg-[#eaf2f8] p-1.5 rounded-full border border-[#d8e6f1]/60">
          <button
            onClick={() => onNavigate('unban')}
            className={`px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              currentPage === 'unban'
                ? 'bg-white text-[#18334a] shadow-xs'
                : 'text-[#486884] hover:text-[#18334a]'
            }`}
          >
            Unbans
          </button>
          <button
            onClick={() => onNavigate('username')}
            className={`px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              currentPage === 'username'
                ? 'bg-white text-[#18334a] shadow-xs'
                : 'text-[#486884] hover:text-[#18334a]'
            }`}
          >
            Usernames
          </button>
          <button
            onClick={() => onNavigate('ban')}
            className={`px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              currentPage === 'ban'
                ? 'bg-white text-[#18334a] shadow-xs'
                : 'text-[#486884] hover:text-[#18334a]'
            }`}
          >
            Ban Requests
          </button>
          <button
            onClick={() => onNavigate('apply')}
            className={`px-4 py-1.5 rounded-full text-xs font-semibold tracking-wide transition-all ${
              currentPage === 'apply'
                ? 'bg-white text-[#18334a] shadow-xs'
                : 'text-[#486884] hover:text-[#18334a]'
            }`}
          >
            Case Review
          </button>
          <button
            onClick={() => onNavigate('admin')}
            className={`px-3 py-1.5 rounded-full text-[11px] font-semibold tracking-wide transition-all flex items-center gap-1 ${
              currentPage === 'admin'
                ? 'bg-[#18334a] text-white shadow-xs'
                : 'text-[#5f7d97] hover:text-[#18334a]'
            }`}
          >
            <ShieldCheck className="w-3 h-3 text-[#599fe0]" />
            Desk
          </button>
        </nav>

        {/* CTA Actions */}
        <div className="flex items-center gap-3">
          <a
            href="https://wa.me/19342012490"
            target="_blank"
            rel="noopener noreferrer"
            className="hidden sm:inline-flex items-center gap-1.5 text-xs font-semibold text-[#315b80] hover:text-[#18334a] px-3.5 py-2 rounded-full border border-[#d2e3f0] hover:border-[#b0cde4] transition-all bg-white shadow-2xs"
          >
            <MessageCircle className="w-3.5 h-3.5 text-[#25D366]" />
            WhatsApp
          </a>
          <button
            onClick={() => onNavigate('apply')}
            className="inline-flex items-center gap-2 text-xs font-semibold text-white bg-[#18334a] hover:bg-[#204360] px-4 py-2.5 rounded-full shadow-sm hover:shadow transition-all group"
          >
            <span>Case Review</span>
            <ArrowUpRight className="w-3.5 h-3.5 text-[#7cb7ea] group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
          </button>
        </div>
      </div>

      {/* Mobile Submenu */}
      <div className="md:hidden flex items-center justify-around py-2 px-3 border-t border-[#e6eff6] bg-[#f8fbfe] text-xs font-medium">
        <button
          onClick={() => onNavigate('unban')}
          className={`px-2.5 py-1 rounded-md ${currentPage === 'unban' ? 'font-bold text-[#18334a]' : 'text-[#597892]'}`}
        >
          Unbans
        </button>
        <button
          onClick={() => onNavigate('username')}
          className={`px-2.5 py-1 rounded-md ${currentPage === 'username' ? 'font-bold text-[#18334a]' : 'text-[#597892]'}`}
        >
          Usernames
        </button>
        <button
          onClick={() => onNavigate('ban')}
          className={`px-2.5 py-1 rounded-md ${currentPage === 'ban' ? 'font-bold text-[#18334a]' : 'text-[#597892]'}`}
        >
          Ban Requests
        </button>
        <button
          onClick={() => onNavigate('admin')}
          className={`px-2 py-1 rounded-md ${currentPage === 'admin' ? 'font-bold text-[#18334a]' : 'text-[#597892]'}`}
        >
          Lead Desk
        </button>
      </div>
    </header>
  );
};
