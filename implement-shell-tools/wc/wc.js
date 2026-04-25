import process, { exit } from "node:process";
import fs from "node:fs";

const argv = process.argv.slice(2);

let showWords = argv.includes("-w");
let showLines = argv.includes("-l");
let showBytes = argv.includes("-c");
let showCharacters = argv.includes("-m");

const filePaths = argv.filter((arg) => !arg.startsWith("-"));
// if no flags enable all.
if (!showLines && !showCharacters && !showWords && !showBytes) {
  showLines = true;
  showCharacters = true;
  showWords = true;
  showBytes = true;
}

if (filePaths.length === 0) {
  console.error("PLease provide a file path");
  process.exit(1);
}

let totalLines = 0;
let totalWords = 0;
let totalBytes = 0;
let totalChars = 0;

filePaths.forEach((filePath) => {
  try {
    const content = fs.readFileSync(filePath, "utf-8");
    const lineArray = content.split("\n");
    if (content.endsWith("\n")) lineArray.pop(); 
    const lines = lineArray.length;
    
    const words = content.trim().split(/\s+/).filter((word) => word != "").length;
    const bytes = Buffer.byteLength(content);
    const characters = content.length;

    totalLines += lines;
    totalWords += words;
    totalBytes += bytes;
    totalChars += characters;

    let output = "";
    if (showLines)   output += lines.toString().padStart(8);
    if (showWords)   output += words.toString().padStart(8);
    if (showBytes)   output += bytes.toString().padStart(8);
    if (showCharacters) output += characters.toString().padStart(8)

    console.log(`${output} ${filePath}`); 
  } catch(error) {
    console.error(`Error reading ${filePath}: ${error.message}`);
  }
}); 

if (filePaths.length > 1) {
  let totalOutput = "";
  if (showLines)  totalOutput += `${totalLines.toString().padStart(8)}`;
  if (showWords)  totalOutput += `${totalWords.toString().padStart(8)}`;
  if (showBytes)  totalOutput += `${totalBytes.toString().padStart(8)}`;
  if (showCharacters) totalOutput += `${totalChars.toString().padStart(8)}`;

  console.log(`${totalOutput} total`);
}
  
