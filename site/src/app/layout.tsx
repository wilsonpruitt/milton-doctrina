import type { Metadata } from "next";
import Link from "next/link";
import {
  EB_Garamond,
  Cormorant_Garamond,
  Cinzel,
  Cinzel_Decorative,
} from "next/font/google";
import { Illumination } from "@/components/decorations";
import "./globals.css";

// next/font self-hosts these at build time — zero CLS, no external request.
const ebGaramond = EB_Garamond({
  subsets: ["latin"],
  weight: ["400", "500", "600"],
  style: ["normal", "italic"],
  variable: "--font-eb-garamond",
  display: "swap",
});

const cormorantGaramond = Cormorant_Garamond({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
  variable: "--font-cormorant-garamond",
  display: "swap",
});

const cinzel = Cinzel({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  variable: "--font-cinzel",
  display: "swap",
});

const cinzelDecorative = Cinzel_Decorative({
  subsets: ["latin"],
  weight: ["400", "700"],
  variable: "--font-cinzel-decorative",
  display: "swap",
});

export const metadata: Metadata = {
  title: "Milton — De Doctrina Christiana (site skeleton, M2)",
  description:
    "A parallel Latin–English edition of John Milton's De Doctrina Christiana, from Sumner's 1825 editio princeps. Development skeleton — not deployed.",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const fontVars = `${ebGaramond.variable} ${cormorantGaramond.variable} ${cinzel.variable} ${cinzelDecorative.variable}`;
  return (
    <html lang="en" className={fontVars}>
      <body>
        <header className="site-header">
          <div className="header-inner">
            <Link href="/" style={{ display: "flex", alignItems: "center", gap: "1rem" }}>
              <Illumination size={54} />
              <div>
                <h1 className="header-title">Milton</h1>
                <p className="header-subtitle">De Doctrina Christiana</p>
              </div>
            </Link>
          </div>
          <nav className="site-nav">
            <Link href="/">Home</Link>
            <Link href="/browse">Browse</Link>
            <Link href="/scripture">Scripture</Link>
            <Link href="/search">Search</Link>
            <Link href="/about">About</Link>
          </nav>
        </header>

        <main className="main-content">{children}</main>

        <footer className="site-footer">
          <p style={{ marginBottom: "0.25rem" }}>Milton De Doctrina Christiana — site skeleton (M2)</p>
          <p style={{ fontSize: "11px", opacity: 0.7 }}>
            Sumner Edition (1825) &middot; Development Skeleton, Not Deployed &middot; MMXXVI
          </p>
        </footer>
      </body>
    </html>
  );
}
