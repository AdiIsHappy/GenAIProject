// app/layout.tsx

import "./globals.css";
import { ReactNode } from "react";

export const metadata = {
  title: "LLM Task Breakdown Tool",
  description: "A tool for breaking down complex tasks using LLMs",
};

export default function RootLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-slate-50">
        <main className="container mx-auto px-4">{children}</main>
      </body>
    </html>
  );
}
