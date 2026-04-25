import fs from "node:fs";
import process from "node:process";

const argv = process.argv.slice(2);

const filePaths = argv.filter((arg) => !arg.startsWith("-"));
const showHiddenFiles = argv.includes("-a");

if (filePaths.length > 1) {
  console.error("Error: This version only supports one directory path a time.");
  process.exit(1);
}

const target = filePaths[0] || ".";

const files = fs.readdirSync(target);

let filteredFIles = files;
if (!showHiddenFiles) {
  filteredFIles = files.filter((file) => !file.startsWith("."));
} else {
  filteredFIles = [".", "..", ...files];
}

filteredFIles.forEach((file) => {
  console.log(file);
});
