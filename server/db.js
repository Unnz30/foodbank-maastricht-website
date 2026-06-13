const mongoose = require("mongoose");

async function connectDatabase() {
  const uri = process.env.MONGODB_URI;

  if (!uri) {
    throw new Error("MONGODB_URI is required. Add it to your local .env file.");
  }

  mongoose.set("strictQuery", true);
  await mongoose.connect(uri);
}

module.exports = { connectDatabase };
