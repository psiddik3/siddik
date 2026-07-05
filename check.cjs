const fs = require("fs");
const html = fs.readFileSync("index.html", "utf8");
const match = html.match(/<script>([\s\S]*?)<\/script>/);
if (match) {
  try {
    new (require("vm").Script)(match[1]);
    console.log("OK");
  } catch(e) {
    console.error(e);
  }
}
