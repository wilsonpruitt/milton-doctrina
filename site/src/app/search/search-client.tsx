"use client";

import { useState } from "react";
import Link from "next/link";

interface SearchEntry {
  id: string;
  title: string;
  bookId: number;
  bookTitle: string;
  chapter: number;
  preview: string;
}

// Fold diacritics, ligatures, and the u/v distinction so queries like
// "veritas" match "ueritas", "æternus", "aeternus", and forms with macrons.
// Lowercase is applied at the call site.
function fold(s: string): string {
  return s
    .normalize("NFKD")
    .replace(/[\u0300-\u036f]/g, "")
    .replace(/æ/g, "ae")
    .replace(/œ/g, "oe")
    .replace(/v/g, "u")
    .replace(/j/g, "i");
}

export function SearchClient({ searchIndex }: { searchIndex: SearchEntry[] }) {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<SearchEntry[]>([]);
  const [searched, setSearched] = useState(false);

  const doSearch = () => {
    const q = query.trim();
    if (!q) {
      setResults([]);
      setSearched(false);
      return;
    }
    const needle = fold(q.toLowerCase());
    setResults(
      searchIndex.filter((entry) => {
        const title = fold(entry.title.toLowerCase());
        const preview = fold(entry.preview.toLowerCase());
        return title.includes(needle) || preview.includes(needle);
      })
    );
    setSearched(true);
  };

  const snippet = (text: string, needleFolded: string): string => {
    if (!text) return "";
    const folded = fold(text.toLowerCase());
    const idx = folded.indexOf(needleFolded);
    if (idx < 0) return text.substring(0, 150) + "…";
    const start = Math.max(0, idx - 60);
    const end = Math.min(text.length, idx + needleFolded.length + 90);
    const prefix = start > 0 ? "…" : "";
    const suffix = end < text.length ? "…" : "";
    return prefix + text.substring(start, end) + suffix;
  };

  const needle = fold(query.trim().toLowerCase());

  return (
    <div>
      <div className="section-title">Search</div>
      <div style={{ display: "flex", gap: "0.5rem", marginBottom: "1.5rem", flexWrap: "wrap" }}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && doSearch()}
          placeholder="Search all languages…"
          className="search-input"
          style={{ flex: "1 1 260px" }}
        />
        <button onClick={doSearch} className="search-btn">
          Search
        </button>
      </div>

      {results.length > 0 && (
        <div>
          <p className="card-meta" style={{ marginBottom: "1rem" }}>
            {results.length} result{results.length !== 1 ? "s" : ""} found
          </p>
          {results.map((r) => (
            <Link key={r.id} href={`/browse/${r.bookId}/${r.chapter}`} className="card-link">
              <div className="card">
                <p
                  style={{
                    fontSize: "12px",
                    color: "#8B6914",
                    fontFamily: "var(--font-cinzel), serif",
                    letterSpacing: "0.08em",
                    marginBottom: "0.25rem",
                  }}
                >
                  {r.bookTitle} &middot; Cap. {r.chapter}
                </p>
                <h3
                  style={{
                    fontFamily: "var(--font-cinzel), serif",
                    fontSize: "15px",
                    fontWeight: 500,
                    color: "#3D1308",
                    marginBottom: "0.5rem",
                  }}
                >
                  {r.title}
                </h3>
                <p style={{ fontSize: "13px", color: "#4A3A2A" }}>{snippet(r.preview, needle)}</p>
              </div>
            </Link>
          ))}
        </div>
      )}

      {searched && results.length === 0 && (
        <p className="body-text" style={{ color: "#6B4A3A", textAlign: "center", margin: "3rem 0" }}>
          No results found for &ldquo;{query}&rdquo;.
        </p>
      )}
    </div>
  );
}
