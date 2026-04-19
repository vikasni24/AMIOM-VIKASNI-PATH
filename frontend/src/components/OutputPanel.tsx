import React from "react";

interface OutputPanelProps {
  title: string;
  content: string;
  isError: boolean;
}

export function OutputPanel({ title, content, isError }: OutputPanelProps) {
  if (!content) return null;

  return (
    <div className={`w-full p-4 rounded-xl bg-surface/80 border ${isError ? 'neon-border-red' : 'neon-border-green'}`}>
      <h3 className={`text-lg font-bold mb-3 ${isError ? 'text-[#ff4d4d] neon-text-glow' : 'text-[#00ff99] neon-text-glow'}`}>
        {title}
      </h3>
      <div className="bg-[#0f172a] p-4 rounded-lg overflow-x-auto">
        <pre className="text-sm font-mono text-gray-300">
          <code>{content}</code>
        </pre>
      </div>
    </div>
  );
}
