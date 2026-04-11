import process from "node:process";
import { promises as fs } from "node:fs";

// THis will give an array without the path to node and to the file.
const argv = process.argv.slice(2);

//Get line numbers.
const showNumbers = argv.includes("-n");
const showNonBlankNumbers = argv.includes("-b");

//filter the - from the array argv as it's a flag.
const filePaths = argv.filter((arg) => !arg.startsWith("-"));

const flagsUsed = argv.filter((arg) => arg.startsWith("-"));
const supportedFlags = ["-n", "-b"];
for (const flag of flagsUsed) {
  if (!supportedFlags.includes(flag)) {
    console.error(`Invalid option try 'node cat.js --help' for more info.`);
    process.exit(1);
  }
}

let counterLines = 1;

for (const path of filePaths) {
  try {
    const content = await fs.readFile(path, "utf-8");

    //split the text at the new line character.
    const splitLines = content.split("\n");

    splitLines.forEach((line) => {
      let prefix = "";

      if (showNonBlankNumbers) {
        if (line.trim() !== "") {
          prefix = `${counterLines++}  `;
        }
      } else if (showNumbers) {
        prefix = `${counterLines++}  `;
      }
      console.log(`${prefix}${line}`);
    });
  } catch (error) {
    console.error(`Could not read: ${path}`);
    process.exit(1);
  }
}
