// import { GoogleGenAI } from "@googel/genai";
import { GoogleGenerativeAI } from "@google/generative-ai";

import wav from "wav";

const GOOGLE_API_KEY = "AIzaSyAc6BnP3GIpJmQ6m3oSSY7S2cDzofsrcCo";
const TEXT_EN =
  "We are a powerful team: Abdullah, AI Engineer; Faisal, Data Scientist; and Ahmad, Full-Stack Developer. Together, we are shaping the future by building an innovative application that leverages AI to revolutionize the entertainment and education sectors.";

async function saveWaveFile(
  filename,
  pcmData,
  channels = 1,
  rate = 24000,
  sampleWidth = 2
) {
  return new Promise((resolve, reject) => {
    const fileWriter = new wav.FileWriter(filename, {
      channels: channels,
      sampleRate: rate,
      bitDepth: sampleWidth * 8,
    });
    fileWriter.on("finish", resolve);
    fileWriter.on("error", reject);
    fileWriter.write(Buffer.from(pcmData));
    fileWriter.end();
  });
}

async function main() {
  const genai = new GoogleGenerativeAI({
    apiKey: "AIzaSyA49kAeKe7-IyPQKiNuijx9Gd4GHBvYwz4",
  });
  const model = genai.getGenerativeModel({ model: "gemini-pro" });
  const response = await model.generateContent({
    contents: [{ parts: [{ text: TEXT_EN }] }],
    config: {
      responseModalities: ["AUDIO"],
      speechConfig: {
        voiceConfig: {
          prebuiltVoiceConfig: { voiceName: "Kore" },
        },
      },
    },
  });
  const data = response.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
  const audioBuffer = Buffer.from(data, "base64");

  const fileName = "TTS_EN-js.wav";
  await saveWaveFile(fileName, audioBuffer);
}
await main();
