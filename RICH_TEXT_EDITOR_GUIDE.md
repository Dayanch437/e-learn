# Rich Text Editor Guide

## ✨ What's New

Your admin panel now includes a powerful **Rich Text Editor** (CKEditor) that allows you to format lesson content with advanced formatting options!

## 🎨 Available Formatting Features

### Text Formatting
- **Bold** - Make text bold
- *Italic* - Italicize text
- <u>Underline</u> - Underline text
- ~~Strikethrough~~ - Strike through text

### Text Alignment
- Left align
- Center align
- Right align
- Justify

### Lists
- Numbered lists (1, 2, 3...)
- Bulleted lists (• points)
- Indent/Outdent list items

### Headings
- Heading 1 (largest)
- Heading 2
- Heading 3
- Heading 4
- Heading 5
- Heading 6 (smallest)
- Paragraph (normal text)

### Advanced Features
- **Links** - Add hyperlinks to external resources
- **Tables** - Create formatted tables
- **Font Size** - Change text size
- **Font Family** - Change font style
- **Text Color** - Change text color
- **Background Color** - Highlight text with background color
- **Horizontal Rule** - Add dividing lines
- **Special Characters** - Insert symbols (©, ®, ™, etc.)
- **Source Code** - View and edit HTML directly

### Editing Tools
- **Undo/Redo** - Reverse or repeat actions
- **Remove Format** - Clear all formatting
- **Maximize** - Expand editor to full screen

## 🚀 How to Use

### Creating a Lesson with Formatting

1. **Go to Admin Panel**: http://localhost:8000/admin
2. **Add/Edit Lesson**: Click on Lessons → Add Lesson (or edit existing)
3. **Use the Toolbar**: You'll see a rich toolbar above the Content field

### Basic Formatting Example

**To make text bold:**
1. Type or select text
2. Click the **B** button in toolbar
3. Text becomes **bold**

**To create a list:**
1. Click numbered list or bullet list icon
2. Type first item
3. Press Enter for next item
4. Press Enter twice to finish list

**To add a heading:**
1. Select your heading text
2. Click "Format" dropdown
3. Choose Heading 1, 2, 3, etc.

**To add a link:**
1. Select text to link
2. Click chain/link icon
3. Enter URL
4. Click OK

### Sample Formatted Content

Here's what you can create:

```
Week 1 - Banking Introduction
=============================

Welcome to Banking Basics!

In this lesson, you will learn:

• Banking fundamentals
• Account types
• Customer service principles

Important Points:

1. Always verify customer identity
2. Maintain confidentiality
3. Provide accurate information

For more information, visit: [Bank Resources](https://example.com)

Note: Complete the quiz by Friday
```

## 💡 Best Practices

### Structure Your Content
- Use **Headings** for main topics
- Use **Bold** for important terms
- Use **Lists** for step-by-step instructions
- Use **Tables** for comparing information

### Keep It Readable
- Don't overuse colors
- Use consistent heading levels
- Break up long paragraphs
- Use lists for clarity

### Professional Formatting
✅ **Do:**
- Use headings to organize
- Bold key concepts
- Create lists for steps
- Add links to resources

❌ **Don't:**
- Use too many colors
- Make everything bold
- Mix fonts randomly
- Use all caps

## 📝 Common Use Cases

### Training Materials
```
Training Objective: Customer Service Excellence

Key Skills:
• Active listening
• Clear communication
• Problem solving

Practice Scenario:
A customer is upset about...
[Continue with formatted content]
```

### Step-by-Step Instructions
```
How to Process a Loan Application

Step 1: Verify Customer Identity
- Check government ID
- Verify address
- Confirm contact information

Step 2: Review Application
[Continue...]
```

### Tables for Comparisons
Use the table button to create:

| Account Type | Interest Rate | Minimum Balance |
|--------------|---------------|-----------------|
| Savings      | 2.5%          | $100           |
| Checking     | 0.5%          | $50            |

## 🔧 Editor Tips

### Keyboard Shortcuts
- **Ctrl+B** - Bold
- **Ctrl+I** - Italic
- **Ctrl+U** - Underline
- **Ctrl+Z** - Undo
- **Ctrl+Y** - Redo
- **Ctrl+L** - Add Link

### Maximize Editor
Click the maximize button (⛶) for full-screen editing - great for long content!

### Source Mode
Click "Source" to see/edit raw HTML if you know HTML

### Copy from Word
You can copy formatted text from Microsoft Word and paste it directly into the editor. The formatting will be preserved!

## 🎯 Examples for Bank Training

### Example 1: Policy Document
```
Banking Security Policy

1. Customer Authentication
   1.1 ID Verification
   1.2 Signature Verification
   1.3 Security Questions

2. Data Protection
   - Use secure systems only
   - Never share passwords
   - Lock workstation when away

Important: Report all security incidents immediately
```

### Example 2: Product Description
```
Premium Savings Account

Features:
• High interest rate (3.5% APY)
• No monthly fees
• Free ATM withdrawals
• Online banking included

Eligibility:
Minimum opening deposit: $1,000
Must maintain $500 balance

For questions, contact: support@bank.com
```

### Example 3: Training Module
```
Module 3: Fraud Prevention

Learning Objectives:
By the end of this module, you will:
✓ Identify common fraud types
✓ Recognize warning signs
✓ Follow proper reporting procedures

Red Flags:
⚠️ Unusual transaction patterns
⚠️ Customer reluctance to provide info
⚠️ Requests to bypass procedures
```

## 🎨 Styling Tips

### Colors for Emphasis
- Use **red** for warnings/important notices
- Use **blue** for links and references  
- Use **green** for success/positive points
- Keep most text in default black

### Text Highlighting
Use background colors sparingly:
- Yellow highlight for key takeaways
- Light blue for tips
- Light red for warnings

## 📱 How Students See Formatted Content

All your formatting (bold, lists, headings, etc.) will display beautifully on the student-facing pages with proper styling!

## ⚠️ Note About CKEditor Version

The editor shows a warning about using an older version. This is fine for:
- Internal bank training systems
- Private networks
- Learning purposes

For internet-facing production systems, consider upgrading to CKEditor 5 later.

## 🆘 Troubleshooting

**Editor not showing?**
- Clear browser cache
- Restart Django server
- Check admin panel in different browser

**Formatting not appearing on student pages?**
- Make sure you saved the lesson
- Refresh the student page
- Check that content field has data

**Lost formatting when pasting?**
- Use "Paste from Word" option if available
- Or paste as plain text and reformat

---

**Now go create beautifully formatted lessons!** 🎓✨
