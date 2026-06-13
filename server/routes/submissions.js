const express = require("express");
const FormSubmission = require("../models/FormSubmission");

const router = express.Router();
const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function clean(value) {
  return typeof value === "string" ? value.trim() : "";
}

function createPublicError(status, message) {
  const error = new Error(message);
  error.status = status;
  error.publicMessage = message;
  return error;
}

function buildSubmission(body, type) {
  const submission = {
    type,
    name: clean(body.name),
    email: clean(body.email).toLowerCase(),
    message: clean(body.message),
    businessName: clean(body.businessName),
    phone: clean(body.phone),
    preferredLanguage: clean(body.preferredLanguage) === "nl" ? "nl" : "en",
    page: clean(body.page)
  };

  if (!submission.name || !submission.email || !submission.message) {
    throw createPublicError(400, "Please fill in your name, email, and message.");
  }

  if (!emailPattern.test(submission.email)) {
    throw createPublicError(400, "Please enter a valid email address.");
  }

  return submission;
}

function asyncRoute(handler) {
  return (req, res, next) => {
    Promise.resolve(handler(req, res)).catch(next);
  };
}

function createSubmissionHandler(type) {
  return asyncRoute(async (req, res) => {
    const submission = buildSubmission(req.body, type);
    const savedSubmission = await FormSubmission.create(submission);

    res.status(201).json({
      ok: true,
      id: savedSubmission.id,
      type: savedSubmission.type
    });
  });
}

router.post("/contact", createSubmissionHandler("contact"));
router.post("/volunteer", createSubmissionHandler("volunteer"));
router.post("/food-donations", createSubmissionHandler("food-donation"));

module.exports = router;
