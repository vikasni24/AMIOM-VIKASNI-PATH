import React from "react";

interface CodeEditorProps {
  code: string;
  setCode: (val: string) => void;
}

export function CodeEditor({ code, setCode }: CodeEditorProps) {
  return (
    <div className="w-full flex flex-col gap-2">
      <label className="text-sm font-semibold text-gray-300">Python Code Input</label>
      <textarea
        value={code}
        onChange={(e) => setCode(e.target.value)}
        className="w-full h-64 p-4 rounded-xl bg-surface border border-gray-700 text-gray-200 font-mono text-sm focus:outline-none focus:neon-border transition shadow-lg resize-y"
        placeholder="Paste your buggy Python code here..."
        spellCheck={false}
      />
    </div>
  );
}
