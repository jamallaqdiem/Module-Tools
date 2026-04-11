import process, { exit } from "node:process";
import fs from "node:fs";

const argv = process.argv.slice(2);

let showWords = argv.includes("-w");
let showLines = argv.includes("-l");
let showBytes = argv.includes("-c");
let showCharacters = argv.includes("-m");

//  filter flags, and getting the string of filename
const filePaths = argv.filter((arg) => !arg.startsWith("-"));
// if no flags enable all.
if (!showLines && !showCharacters && !showWords && !showBytes) {
  showLines = true;
  showCharacters = true;
  showWords = true;
  showBytes = true;
}
// fix bug .length ===0 will be true if nothing provided, instead !filePath will return empty array which result true.
if (filePaths.length === 0) {
  console.error("PLease provide a file path");
  process.exit(1);
}
// loop trough the array to get each file path.
filePaths.forEach((filePath) => {
  const content = fs.readFileSync(filePath, "utf-8");

  const lines = content.split("\n").length - 1;
  const words = content
    .trim()
    .split(/\s+/)
    .filter((word) => word != "").length;
  // here I used Buffer.byteLength even if characters and bytes can be the same number .length, however sometimes an emoji or special characters can be heavier 2b or 4b
  const bytes = Buffer.byteLength(content);
  const characters = content.length;

  let output = "";

  if (showLines) output += `${lines} `;
  if (showWords) output += `${words} `;
  if (showBytes) output += `${bytes} `;
  if (showCharacters) output += `${characters} `;

  console.log(`${output} ${filePath}`);
});
