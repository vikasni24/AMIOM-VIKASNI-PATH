import React from "react";
import { Loader2 } from "lucide-react";

interface RunButtonProps {
  onClick: () => void;
  isLoading: boolean;
}

export function RunButton({ onClick, isLoading }: RunButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={isLoading}
      className="w-full md:w-auto px-8 py-3 rounded-xl bg-primary text-white font-bold text-lg 
                 shadow-[0_0_15px_#8F113B] hover:shadow-[0_0_25px_#b3154a] hover:scale-105 transition-all
                 disabled:opacity-70 disabled:hover:scale-100 disabled:shadow-none flex items-center justify-center gap-2"
    >
      {isLoading ? (
        <>
          <Loader2 className="animate-spin" size={20} />
          AI is analyzing your code...
        </>
      ) : (
        "Run AI Debugger"
      )}
    </button>
  );
}
