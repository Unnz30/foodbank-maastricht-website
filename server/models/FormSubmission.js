const mongoose = require("mongoose");

const formSubmissionSchema = new mongoose.Schema(
  {
    type: {
      type: String,
      enum: ["contact", "volunteer", "food-donation"],
      required: true,
      index: true
    },
    name: {
      type: String,
      required: true,
      trim: true,
      maxlength: 120
    },
    email: {
      type: String,
      required: true,
      trim: true,
      lowercase: true,
      maxlength: 254
    },
    message: {
      type: String,
      required: true,
      trim: true,
      maxlength: 2000
    },
    businessName: {
      type: String,
      trim: true,
      maxlength: 160
    },
    phone: {
      type: String,
      trim: true,
      maxlength: 60
    },
    preferredLanguage: {
      type: String,
      enum: ["en", "nl"],
      default: "en"
    },
    page: {
      type: String,
      trim: true,
      maxlength: 160
    }
  },
  { timestamps: true }
);

module.exports = mongoose.model("FormSubmission", formSubmissionSchema);
