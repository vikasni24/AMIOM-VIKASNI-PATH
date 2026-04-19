export async function runDebugger(code: string, model: string) {
  try {
    const response = await fetch("http://localhost:8000/api/debug", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        code,
        model,
      }),
    });

    if (!response.ok) {
      throw new Error("Failed to communicate with debugging server");
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error("API Error:", error);
    throw error;
  }
}
