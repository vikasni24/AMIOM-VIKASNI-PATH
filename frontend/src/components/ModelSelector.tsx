"use client";
import React from "react";
import { Select } from "@/components/Select";

interface ModelSelectorProps {
  model: string;
  setModel: (val: string) => void;
}

export function ModelSelector({ model, setModel }: ModelSelectorProps) {
  const options = [
    { label: "Llama 3.3 70B Versatile", value: "llama-3.3-70b-versatile" },
    { label: "Llama 3.1 8B Instant", value: "llama-3.1-8b-instant" },
  ];

  return (
    <div className="w-full flex flex-col gap-2 max-w-sm">
      <label className="text-sm font-semibold text-gray-300">Select AI Model</label>
      <Select
        value={model}
        onChange={setModel}
        options={options}
        placeholder="Select a model..."
      />
    </div>
  );
}
