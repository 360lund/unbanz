import React, { useState, useEffect, useMemo } from 'react';
import { LeadItem, PageView } from '../types';
import {
  Shield,
  Search,
  RotateCcw,
  CheckCircle,
  Clock,
  Inbox,
  X,
  ExternalLink,
  ChevronRight,
  Eye,
  EyeOff,
  User,
  Mail,
  Phone,
  FileText,
  AlertCircle
} from 'lucide-react';

interface AdminDeskProps {
  onNavigate: (page: PageView) => void;
}

export const AdminDesk: React.FC<AdminDeskProps> = ({ onNavigate }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [authError, setAuthError] = useState('');

  const [leads, setLeads] = useState<LeadItem[]>([]);
  const [activeFilter, setActiveFilter] = useState<'All' | 'New' | 'In progress' | 'Closed'>('All');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedLead, setSelectedLead] = useState<LeadItem | null>(null);

  // Edit fields for selected lead
  const [editStatus, setEditStatus] = useState<'New' | 'In progress' | 'Closed'>('New');
  const [editNote, setEditNote] = useState('');
  const [saveStatusMessage, setSaveStatusMessage] = useState('');
  const [isSaving, setIsSaving] = useState(false);

  // Fetch leads from backend
  const fetchLeads = async () => {
    try {
      const res = await fetch('/api/leads');
      if (res.ok) {
        const data = await res.json();
        setLeads(data.leads || []);
      }
    } catch {
      // ignore
    }
  };

  useEffect(() => {
    fetchLeads();
  }, []);

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault();
    if (password === 'preview') {
      setIsAuthenticated(true);
      setAuthError('');
      fetchLeads();
    } else {
      setAuthError('Incorrect password. Use "preview" to access the demo desk.');
    }
  };

  const handleResetDemo = async () => {
    try {
      const res = await fetch('/api/leads/reset', { method: 'POST' });
      if (res.ok) {
        const data = await res.json();
        setLeads(data.leads || []);
        setActiveFilter('All');
        setSearchQuery('');
      }
    } catch {
      // ignore
    }
  };

  const handleOpenLead = (lead: LeadItem) => {
    setSelectedLead(lead);
    setEditStatus(lead.status);
    setEditNote(lead.note || '');
    setSaveStatusMessage('');
  };

  const handleSaveLead = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedLead) return;

    setIsSaving(true);
    try {
      const res = await fetch(`/api/leads/${selectedLead.id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          status: editStatus,
          note: editNote
        })
      });

      if (res.ok) {
        setLeads((prev) =>
          prev.map((l) =>
            l.id === selectedLead.id
              ? { ...l, status: editStatus, note: editNote }
              : l
          )
        );
        setSelectedLead((prev) =>
          prev ? { ...prev, status: editStatus, note: editNote } : null
        );
        setSaveStatusMessage('Lead updated successfully!');
      } else {
        setSaveStatusMessage('Could not save changes.');
      }
    } catch {
      setSaveStatusMessage('Network error while saving.');
    } finally {
      setIsSaving(false);
    }
  };

  const filteredLeads = useMemo(() => {
    return leads.filter((l) => {
      const matchesFilter = activeFilter === 'All' || l.status === activeFilter;
      const q = searchQuery.toLowerCase().trim();
      const matchesSearch =
        !q ||
        l.name.toLowerCase().includes(q) ||
        l.handle.toLowerCase().includes(q) ||
        l.service.toLowerCase().includes(q) ||
        l.email.toLowerCase().includes(q);
      return matchesFilter && matchesSearch;
    });
  }, [leads, activeFilter, searchQuery]);

  const metrics = useMemo(() => {
    return {
      total: leads.length,
      newCount: leads.filter((l) => l.status === 'New').length,
      progressCount: leads.filter((l) => l.status === 'In progress').length,
      closedCount: leads.filter((l) => l.status === 'Closed').length
    };
  }, [leads]);

  const getInitials = (name: string) => {
    return name
      .split(' ')
      .map((n) => n[0])
      .slice(0, 2)
      .join('')
      .toUpperCase();
  };

  // If not logged in, render preview login
  if (!isAuthenticated) {
    return (
      <div className="min-h-[80vh] flex flex-col justify-center items-center px-4 py-12">
        <div className="w-full max-w-md bg-white rounded-3xl p-8 border border-[#dce8f2] shadow-sm">
          <div className="flex items-center gap-2 mb-8">
            <div className="w-8 h-8 rounded-xl bg-[#599fe0] flex items-center justify-center text-white font-bold text-lg">
              u.
            </div>
            <span className="text-2xl font-bold tracking-tight text-[#18334a]">
              unbanz<span className="text-[#599fe0]">.</span>
            </span>
          </div>

          <span className="text-[10px] font-bold uppercase tracking-wider text-[#698ea9] block mb-1">
            Lead Desk Access
          </span>
          <h2 className="text-3xl font-extrabold text-[#18334a] tracking-tight leading-tight mb-2">
            Good to have you back.
          </h2>
          <p className="text-xs text-[#527390] mb-6">
            Review case enquiries, update status, and manage client applications.
          </p>

          <form onSubmit={handleLogin} className="space-y-4">
            <div>
              <label className="block text-xs font-semibold text-[#355776] mb-1.5">
                Preview password
              </label>
              <div className="relative">
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  placeholder="Enter preview password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-[#18334a] text-sm rounded-xl px-4 py-3 pr-14 focus:outline-none focus:ring-2 focus:ring-[#599fe0] transition-all"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3.5 top-1/2 -translate-y-1/2 text-xs font-semibold text-[#658ba9] hover:text-[#18334a] cursor-pointer"
                >
                  {showPassword ? 'Hide' : 'Show'}
                </button>
              </div>
            </div>

            {authError && (
              <p className="text-xs text-[#c0392b] font-medium flex items-center gap-1.5">
                <AlertCircle className="w-3.5 h-3.5" />
                {authError}
              </p>
            )}

            <button
              type="submit"
              className="w-full py-3.5 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-xs font-bold transition-all shadow-sm cursor-pointer"
            >
              Open Lead Desk ↗
            </button>
          </form>

          <div className="mt-6 pt-5 border-t border-[#edf4fa] text-[11px] text-[#7192ac] space-y-1">
            <p>
              Design preview · password: <strong className="text-[#18334a]">preview</strong>
            </p>
            <p className="text-[10px] text-[#8ea7bc]">
              Explore sample leads or test case submissions in real time.
            </p>
          </div>
        </div>
      </div>
    );
  }

  // Authenticated workspace
  return (
    <div className="min-h-screen bg-[#f5f9fc] flex flex-col md:flex-row border-t border-[#e2ecf5]">
      {/* Sidebar */}
      <aside className="w-full md:w-64 bg-[#18334a] text-[#c3daeb] p-6 flex flex-col justify-between shrink-0">
        <div>
          <div className="flex items-center justify-between mb-8">
            <div className="flex items-center gap-2">
              <div className="w-7 h-7 rounded-lg bg-[#599fe0] flex items-center justify-center text-white font-bold text-sm">
                u.
              </div>
              <span className="text-xl font-bold text-white tracking-tight">
                unbanz.
              </span>
            </div>
            <span className="text-[10px] font-bold bg-[#264b6b] text-[#86b5db] px-2 py-0.5 rounded">
              DEMO
            </span>
          </div>

          <p className="text-[10px] font-bold uppercase tracking-wider text-[#6992b4] mb-3">
            WORKSPACE
          </p>

          <nav className="space-y-1 text-xs">
            <button
              onClick={() => setActiveFilter('All')}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl font-medium transition-colors cursor-pointer ${
                activeFilter === 'All'
                  ? 'bg-[#295175] text-white font-semibold'
                  : 'hover:bg-[#204362] text-[#a1c4df]'
              }`}
            >
              <span className="flex items-center gap-2.5">
                <Inbox className="w-4 h-4 text-[#599fe0]" />
                Lead Inbox
              </span>
              <span className="text-[11px] bg-[#36618a] px-2 py-0.5 rounded-full text-white">
                {metrics.total}
              </span>
            </button>

            <button
              onClick={() => setActiveFilter('New')}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl font-medium transition-colors cursor-pointer ${
                activeFilter === 'New'
                  ? 'bg-[#295175] text-white font-semibold'
                  : 'hover:bg-[#204362] text-[#a1c4df]'
              }`}
            >
              <span className="flex items-center gap-2.5">
                <span className="w-2 h-2 rounded-full bg-[#599fe0]" />
                New Enquiries
              </span>
              <span className="text-[11px] text-[#9cc4e4]">{metrics.newCount}</span>
            </button>

            <button
              onClick={() => setActiveFilter('In progress')}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl font-medium transition-colors cursor-pointer ${
                activeFilter === 'In progress'
                  ? 'bg-[#295175] text-white font-semibold'
                  : 'hover:bg-[#204362] text-[#a1c4df]'
              }`}
            >
              <span className="flex items-center gap-2.5">
                <Clock className="w-3.5 h-3.5 text-[#eab308]" />
                In Progress
              </span>
              <span className="text-[11px] text-[#9cc4e4]">{metrics.progressCount}</span>
            </button>

            <button
              onClick={() => setActiveFilter('Closed')}
              className={`w-full flex items-center justify-between px-3 py-2.5 rounded-xl font-medium transition-colors cursor-pointer ${
                activeFilter === 'Closed'
                  ? 'bg-[#295175] text-white font-semibold'
                  : 'hover:bg-[#204362] text-[#a1c4df]'
              }`}
            >
              <span className="flex items-center gap-2.5">
                <CheckCircle className="w-3.5 h-3.5 text-[#22c55e]" />
                Closed Cases
              </span>
              <span className="text-[11px] text-[#9cc4e4]">{metrics.closedCount}</span>
            </button>
          </nav>
        </div>

        <div className="pt-6 border-t border-[#234664] text-xs">
          <p className="text-[11px] text-[#7ba5c8] mb-3">
            Design Preview Desk
          </p>
          <button
            onClick={() => setIsAuthenticated(false)}
            className="text-xs text-[#a5cceb] hover:text-white transition-colors cursor-pointer flex items-center gap-1.5"
          >
            <span>Leave preview</span>
            <ExternalLink className="w-3 h-3" />
          </button>
        </div>
      </aside>

      {/* Main Content Area */}
      <main className="flex-1 p-6 md:p-10 max-w-6xl">
        {/* Top bar */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-8 border-b border-[#dce8f2]">
          <div>
            <p className="text-[10px] font-bold uppercase tracking-wider text-[#599fe0] mb-1">
              WORKSPACE / LEADS
            </p>
            <h1 className="text-3xl font-extrabold text-[#18334a] tracking-tight">
              Your leads. Your next move.
            </h1>
            <p className="text-xs text-[#527390] mt-1">
              Review case enquiries and prioritize escalations.
            </p>
          </div>

          <div className="flex items-center gap-3">
            <button
              onClick={handleResetDemo}
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-white border border-[#d2e2f0] text-xs font-semibold text-[#315679] hover:bg-[#f0f6fb] transition-colors cursor-pointer"
            >
              <RotateCcw className="w-3.5 h-3.5 text-[#599fe0]" />
              Reset Demo
            </button>
            <div className="flex items-center gap-2 bg-white px-3 py-1.5 rounded-full border border-[#d2e2f0]">
              <div className="w-6 h-6 rounded-full bg-[#599fe0] text-white flex items-center justify-center text-[10px] font-bold">
                AB
              </div>
              <span className="text-xs font-semibold text-[#18334a]">Admin</span>
            </div>
          </div>
        </div>

        {/* Metrics Row */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 my-8">
          <div className="bg-white p-5 rounded-2xl border border-[#dce8f2] shadow-2xs">
            <span className="text-xs text-[#63849f] font-medium">Total Leads</span>
            <p className="text-3xl font-extrabold text-[#18334a] mt-2 mb-1">{metrics.total}</p>
            <span className="text-[10px] text-[#86a3bc]">All demo enquiries</span>
          </div>

          <div className="bg-white p-5 rounded-2xl border border-[#dce8f2] shadow-2xs">
            <span className="text-xs text-[#63849f] font-medium">New Enquiries</span>
            <p className="text-3xl font-extrabold text-[#18334a] mt-2 mb-1">{metrics.newCount}</p>
            <span className="text-[10px] text-[#86a3bc]">Ready for case review</span>
          </div>

          <div className="bg-white p-5 rounded-2xl border border-[#dce8f2] shadow-2xs">
            <span className="text-xs text-[#63849f] font-medium">In Progress</span>
            <p className="text-3xl font-extrabold text-[#18334a] mt-2 mb-1">{metrics.progressCount}</p>
            <span className="text-[10px] text-[#86a3bc]">Escalation underway</span>
          </div>

          <div className="bg-white p-5 rounded-2xl border border-[#dce8f2] shadow-2xs">
            <span className="text-xs text-[#63849f] font-medium">Closed Cases</span>
            <p className="text-3xl font-extrabold text-[#18334a] mt-2 mb-1">{metrics.closedCount}</p>
            <span className="text-[10px] text-[#86a3bc]">Resolved or concluded</span>
          </div>
        </div>

        {/* Lead Inbox Table & Filters */}
        <div className="bg-white rounded-2xl border border-[#dce8f2] shadow-xs overflow-hidden">
          <div className="p-6 border-b border-[#edf4fa] flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <h2 className="text-lg font-bold text-[#18334a] flex items-center gap-2">
                <span>Lead Inbox</span>
                <span className="text-xs bg-[#eaf4fb] text-[#2c5b85] font-semibold px-2 py-0.5 rounded-full">
                  {filteredLeads.length} visible
                </span>
              </h2>
              <p className="text-xs text-[#60829f] mt-0.5">
                Select any lead to inspect details, add notes, or change status.
              </p>
            </div>

            <div className="flex flex-wrap items-center gap-3">
              {/* Search input */}
              <div className="relative">
                <Search className="w-3.5 h-3.5 text-[#7394ae] absolute left-3 top-1/2 -translate-y-1/2" />
                <input
                  type="text"
                  placeholder="Search name, account, service..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="bg-[#f8fbfe] border border-[#d5e4f2] text-xs rounded-xl pl-9 pr-3 py-2 text-[#18334a] focus:outline-none focus:ring-2 focus:ring-[#599fe0] w-64"
                />
              </div>

              {/* Status pills */}
              <div className="flex items-center gap-1 bg-[#f4f8fc] p-1 rounded-xl border border-[#dbe8f3]">
                {(['All', 'New', 'In progress', 'Closed'] as const).map((filter) => (
                  <button
                    key={filter}
                    onClick={() => setActiveFilter(filter)}
                    className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
                      activeFilter === filter
                        ? 'bg-white text-[#18334a] shadow-2xs'
                        : 'text-[#64849f] hover:text-[#18334a]'
                    }`}
                  >
                    {filter}
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Lead List */}
          <div className="divide-y divide-[#edf4fa]">
            {filteredLeads.length === 0 ? (
              <div className="p-12 text-center text-xs text-[#708fa8]">
                No leads match your filter or search query.
              </div>
            ) : (
              filteredLeads.map((lead) => (
                <div
                  key={lead.id}
                  onClick={() => handleOpenLead(lead)}
                  className="p-4 sm:px-6 hover:bg-[#f6faff] transition-colors cursor-pointer flex items-center justify-between gap-4 group"
                >
                  <div className="flex items-center gap-3 min-w-0">
                    <div className="w-9 h-9 rounded-full bg-[#eaf4fb] text-[#2c5b85] font-bold text-xs flex items-center justify-center shrink-0">
                      {getInitials(lead.name)}
                    </div>
                    <div className="min-w-0">
                      <div className="flex items-center gap-2">
                        <strong className="text-xs font-semibold text-[#18334a] truncate">
                          {lead.name}
                        </strong>
                        <span className="text-[11px] text-[#698ba7] font-mono truncate">
                          {lead.handle}
                        </span>
                      </div>
                      <p className="text-[11px] text-[#7193ae] truncate mt-0.5">
                        {lead.service}
                      </p>
                    </div>
                  </div>

                  <div className="flex items-center gap-4 shrink-0">
                    <span
                      className={`text-[11px] font-semibold px-2.5 py-1 rounded-full ${
                        lead.status === 'New'
                          ? 'bg-[#eaf3fb] text-[#2c6591]'
                          : lead.status === 'In progress'
                            ? 'bg-[#fef9c3] text-[#854d0e]'
                            : 'bg-[#eaf5ef] text-[#1c6742]'
                      }`}
                    >
                      {lead.status}
                    </span>
                    <span className="text-[11px] text-[#86a2b8] hidden sm:inline-block">
                      {lead.date}
                    </span>
                    <ChevronRight className="w-4 h-4 text-[#9ab7cf] group-hover:text-[#18334a] group-hover:translate-x-0.5 transition-all" />
                  </div>
                </div>
              ))
            )}
          </div>
        </div>
      </main>

      {/* Lead Detail Modal Dialog */}
      {selectedLead && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-[#15354c]/50 backdrop-blur-xs">
          <div className="bg-white rounded-3xl w-full max-w-xl max-h-[90vh] overflow-y-auto p-6 sm:p-8 border border-[#dce8f2] shadow-2xl animate-in fade-in zoom-in-95 duration-150">
            {/* Modal Header */}
            <div className="flex items-center justify-between pb-4 border-b border-[#edf4fa]">
              <span className="text-[10px] font-bold uppercase tracking-wider text-[#599fe0]">
                LEAD DOSSIER · DEMO
              </span>
              <button
                onClick={() => setSelectedLead(null)}
                className="w-8 h-8 rounded-full bg-[#f4f8fc] hover:bg-[#eaf2f8] flex items-center justify-center text-[#557794] hover:text-[#18334a] transition-colors cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* Person profile banner */}
            <div className="flex items-center gap-4 my-6">
              <div className="w-14 h-14 rounded-2xl bg-[#eaf4fb] text-[#2c5b85] font-bold text-xl flex items-center justify-center shrink-0">
                {getInitials(selectedLead.name)}
              </div>
              <div>
                <h3 className="text-xl font-bold text-[#18334a]">
                  {selectedLead.name}
                </h3>
                <p className="text-xs text-[#599fe0] font-mono mt-0.5">
                  {selectedLead.handle}
                </p>
              </div>
            </div>

            {/* Info Grid */}
            <div className="grid grid-cols-2 gap-4 bg-[#f8fbfe] p-4 rounded-2xl border border-[#e2edf6] text-xs mb-6">
              <div>
                <span className="text-[10px] text-[#698ba7] uppercase font-bold tracking-wider">
                  Service
                </span>
                <p className="font-semibold text-[#18334a] mt-0.5">
                  {selectedLead.service}
                </p>
              </div>

              <div>
                <span className="text-[10px] text-[#698ba7] uppercase font-bold tracking-wider">
                  Received
                </span>
                <p className="font-semibold text-[#18334a] mt-0.5">
                  {selectedLead.date}
                </p>
              </div>

              <div>
                <span className="text-[10px] text-[#698ba7] uppercase font-bold tracking-wider">
                  Email
                </span>
                <p className="font-semibold text-[#18334a] mt-0.5 break-all">
                  {selectedLead.email}
                </p>
              </div>

              <div>
                <span className="text-[10px] text-[#698ba7] uppercase font-bold tracking-wider">
                  Phone
                </span>
                <p className="font-semibold text-[#18334a] mt-0.5">
                  {selectedLead.phone}
                </p>
              </div>
            </div>

            {/* Message / Background */}
            <div className="mb-6">
              <span className="text-[10px] text-[#698ba7] uppercase font-bold tracking-wider block mb-1.5">
                The Request / Violation Statement
              </span>
              <div className="bg-[#edf5fa] rounded-2xl p-4 text-xs text-[#315679] leading-relaxed">
                {selectedLead.message}
              </div>
            </div>

            {/* Lead Status & Note Edit Form */}
            <form onSubmit={handleSaveLead} className="space-y-4 pt-4 border-t border-[#edf4fa]">
              <div>
                <label className="block text-xs font-bold text-[#355776] mb-1.5">
                  Update Lead Status
                </label>
                <select
                  value={editStatus}
                  onChange={(e) => setEditStatus(e.target.value as 'New' | 'In progress' | 'Closed')}
                  className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-xs font-semibold rounded-xl px-4 py-2.5 text-[#18334a] focus:outline-none focus:ring-2 focus:ring-[#599fe0]"
                >
                  <option value="New">New</option>
                  <option value="In progress">In progress</option>
                  <option value="Closed">Closed</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-[#355776] mb-1.5">
                  Specialist Internal Note
                </label>
                <textarea
                  rows={3}
                  placeholder="Record policy escalation details, representative contact, or case resolution notes..."
                  value={editNote}
                  onChange={(e) => setEditNote(e.target.value)}
                  className="w-full bg-[#f8fbfe] border border-[#d5e4f2] text-xs rounded-xl p-3 text-[#18334a] focus:outline-none focus:ring-2 focus:ring-[#599fe0] resize-y"
                />
              </div>

              {saveStatusMessage && (
                <p className="text-xs text-[#1c6742] font-semibold">
                  {saveStatusMessage}
                </p>
              )}

              <div className="flex items-center justify-end gap-3 pt-2">
                <button
                  type="button"
                  onClick={() => setSelectedLead(null)}
                  className="px-4 py-2 rounded-xl text-xs font-semibold text-[#5a7c98] hover:bg-[#f0f6fb] transition-colors cursor-pointer"
                >
                  Close
                </button>
                <button
                  type="submit"
                  disabled={isSaving}
                  className="px-5 py-2.5 rounded-full bg-[#18334a] hover:bg-[#224766] text-white text-xs font-bold transition-all shadow-xs cursor-pointer disabled:opacity-50"
                >
                  {isSaving ? 'Saving...' : 'Save Lead Changes ✓'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
};
