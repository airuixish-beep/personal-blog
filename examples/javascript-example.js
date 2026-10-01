// Minimal AI API learning example.
// Uses placeholder values so no real credentials are committed.

const apiUrl = process.env.AI_API_URL || "https://example.com/v1/chat";
const apiKey = process.env.AI_API_KEY;

if (!apiKey) {
  throw new Error("Set AI_API_KEY in your environment before running this example.");
}

const response = await fetch(apiUrl, {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${apiKey}`,
  },
  body: JSON.stringify({
    model: "example-model",
    messages: [
      { role: "user", content: "Explain context windows in simple language." },
    ],
  }),
});

if (!response.ok) {
  throw new Error(`Request failed: ${response.status}`);
}

console.log(await response.json());
