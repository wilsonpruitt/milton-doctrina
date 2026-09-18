import type { MetadataRoute } from "next";
import { loadAllContent } from "@/lib/content";
import scriptureIndex from "@/data/scripture/index.json";

const BASE = "https://milton.wrootpress.com";

// Mirrors the generateStaticParams of every route so the sitemap and the
// exported pages cannot drift apart.
export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  const urls: string[] = ["/", "/about", "/browse", "/scripture", "/search", "/rights", "/export"];

  const books = loadAllContent();
  for (const book of books) {
    urls.push(`/browse/${book.id}`);
    for (const chapter of book.chapters) {
      urls.push(`/browse/${book.id}/${chapter.chapter}`);
    }
  }

  for (const b of (scriptureIndex as { books: { slug: string }[] }).books) {
    urls.push(`/scripture/${b.slug}`);
  }

  return urls.map((url) => ({ url: `${BASE}${url}` }));
}
