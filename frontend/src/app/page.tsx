"use client";
import React, { useState } from "react";
import { CodeEditor } from "@/components/CodeEditor";
import { ModelSelector } from "@/components/ModelSelector";
import { RunButton } from "@/components/RunButton";
import { OutputPanel } from "@/components/OutputPanel";
import { runDebugger } from "@/lib/api";

export default function Dashboard() {
  const [code, setCode] = useState<string>("");
  const [model, setModel] = useState<string>("llama-3.3-70b-versatile");
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [errorDetails, setErrorDetails] = useState<string>("");
  const [fixedCode, setFixedCode] = useState<string>("");

  const handleRun = async () => {
    if (!code.trim()) return;

    setIsLoading(true);
    setErrorDetails("");
    setFixedCode("");

    try {
      const result = await runDebugger(code, model);
      if (result.error) {
        setErrorDetails(result.error);
        setFixedCode(result.fixed_code);
      } else {
        setFixedCode("No errors detected! Your code runs perfectly.\n\n" + result.fixed_code);
      }
    } catch (err: any) {
      setErrorDetails(err.message || "An unexpected error occurred.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen w-full flex flex-col p-8 lg:px-24 xl:px-48">
      <header className="mb-10 text-center">
        <h1 className="text-4xl md:text-6xl font-extrabold text-[#00ffff] neon-text-glow tracking-tight">
          Self Correction AI Agent
        </h1>
        <p className="mt-2 text-gray-400">Autonomous Python Debugger & AI Fixer</p>
      </header>

      <div className="flex flex-col gap-6">
        <CodeEditor code={code} setCode={setCode} />
        
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-4">
          <ModelSelector model={model} setModel={setModel} />
          <RunButton onClick={handleRun} isLoading={isLoading} />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">
          <div className="col-span-1">
            <OutputPanel title="Error Output" content={errorDetails} isError={true} />
          </div>
          <div className="col-span-1">
            <OutputPanel title="AI Fixed Code" content={fixedCode} isError={false} />
          </div>
        </div>
      </div>
    </main>
  );
}
