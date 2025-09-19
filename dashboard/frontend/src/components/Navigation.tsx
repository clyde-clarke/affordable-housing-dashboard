import React from 'react';

interface NavigationProps {
  pages: Array<{
    id: string;
    title: string;
    component: React.ComponentType;
  }>;
  currentPage: string;
  onPageChange: (pageId: string) => void;
}

const Navigation: React.FC<NavigationProps> = ({ pages, currentPage, onPageChange }) => {
  return (
    <nav className="nav-container">
      <ul className="nav-list">
        {pages.map((page) => (
          <li
            key={page.id}
            className={`nav-item ${currentPage === page.id ? 'active' : ''}`}
            onClick={() => onPageChange(page.id)}
          >
            {page.title}
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Navigation;
