import React, { useState, useEffect } from 'react';
import { PageView } from './types';
import { Header } from './components/Header';
import { Footer } from './components/Footer';
import { HomePage } from './pages/HomePage';
import { UnbanPage } from './pages/UnbanPage';
import { UsernamePage } from './pages/UsernamePage';
import { BanPage } from './pages/BanPage';
import { ApplyPage } from './pages/ApplyPage';
import { AdminDesk } from './pages/AdminDesk';

export const App: React.FC = () => {
  const [currentPage, setCurrentPage] = useState<PageView>('home');
  const [selectedService, setSelectedService] = useState<string | undefined>(undefined);

  // Parse path on initial load & popstate
  useEffect(() => {
    const handleLocationChange = () => {
      const path = window.location.pathname.replace(/\/$/, '') || '/';
      const searchParams = new URLSearchParams(window.location.search);
      const s = searchParams.get('service');

      if (s) setSelectedService(s);

      if (path === '/' || path === '') {
        setCurrentPage('home');
      } else if (path === '/unban') {
        setCurrentPage('unban');
      } else if (path === '/username') {
        setCurrentPage('username');
      } else if (path === '/ban') {
        setCurrentPage('ban');
      } else if (path === '/apply') {
        setCurrentPage('apply');
      } else if (path === '/admin') {
        setCurrentPage('admin');
      } else {
        setCurrentPage('home');
      }
    };

    handleLocationChange();
    window.addEventListener('popstate', handleLocationChange);
    return () => window.removeEventListener('popstate', handleLocationChange);
  }, []);

  const handleNavigate = (page: PageView, params?: { service?: string }) => {
    setCurrentPage(page);
    if (params?.service) {
      setSelectedService(params.service);
    } else {
      setSelectedService(undefined);
    }

    let targetPath = '/';
    if (page === 'unban') targetPath = '/unban';
    else if (page === 'username') targetPath = '/username';
    else if (page === 'ban') targetPath = '/ban';
    else if (page === 'apply') targetPath = '/apply';
    else if (page === 'admin') targetPath = '/admin';

    const queryString = params?.service ? `?service=${encodeURIComponent(params.service)}` : '';
    window.history.pushState({}, '', targetPath + queryString);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="min-h-screen flex flex-col bg-[#f5f9fc] text-[#18334a]">
      <Header currentPage={currentPage} onNavigate={handleNavigate} />

      <main className="flex-1">
        {currentPage === 'home' && <HomePage onNavigate={handleNavigate} />}
        {currentPage === 'unban' && <UnbanPage onNavigate={handleNavigate} />}
        {currentPage === 'username' && <UsernamePage onNavigate={handleNavigate} />}
        {currentPage === 'ban' && <BanPage onNavigate={handleNavigate} />}
        {currentPage === 'apply' && (
          <ApplyPage initialService={selectedService} onNavigate={handleNavigate} />
        )}
        {currentPage === 'admin' && <AdminDesk onNavigate={handleNavigate} />}
      </main>

      <Footer onNavigate={handleNavigate} />
    </div>
  );
};

export default App;
