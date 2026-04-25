import process from "node:process";
import { promises as fs } from "node:fs";

const argv = process.argv.slice(2);

const showNumbers = argv.includes("-n");
const showNonBlankNumbers = argv.includes("-b");

const filePaths = argv.filter((arg) => !arg.startsWith("-"));

const flagsUsed = argv.filter((arg) => arg.startsWith("-"));
const supportedFlags = ["-n", "-b"];
for (const flag of flagsUsed) {
  if (!supportedFlags.includes(flag)) {
    console.error(`Invalid option: please try "-n or "-b"`);
    process.exit(1);
  }
}

let counterLines = 1;

for (const path of filePaths) {
  try {
    const content = await fs.readFile(path, "utf-8");
.
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
    console.error(`Error ${path}: ${error.message}`);
    process.exit(1);
  }
}
