"""
Sample data creation script for testing the lesson manager.
Run this after creating a superuser to populate the database with sample lessons.

Usage:
    python create_sample_data.py
"""

import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lesson_manager.settings')
django.setup()

from lessons.models import Lesson
from django.utils import timezone


def create_sample_lessons():
    """Create sample lessons for testing"""
    
    print("Creating sample lessons...")
    
    # Sample lesson data
    lessons_data = [
        {
            'title': 'Week 1: Introduction to Banking',
            'description': 'Overview of banking industry, key concepts, and fundamental principles.',
            'content': '''Welcome to Banking Basics!

In this first week, we will cover:

1. What is Banking?
   - Definition and purpose
   - Types of banks
   - Banking services overview

2. Key Banking Concepts
   - Deposits and withdrawals
   - Interest rates
   - Account types

3. Regulatory Environment
   - Banking regulations
   - Customer protection
   - Compliance basics

Please review all materials and complete the quiz by Friday.''',
            'order': 10,
            'is_published': True
        },
        {
            'title': 'Week 2: Customer Service Excellence',
            'description': 'Learn professional customer service techniques specific to banking.',
            'content': '''Customer Service in Banking

This week focuses on building excellent customer service skills:

Topics:
- Communication techniques
- Handling difficult customers
- Professional phone etiquette
- Email communication standards
- Building customer trust

Key Points:
- Always greet customers warmly
- Listen actively to their needs
- Provide clear, accurate information
- Follow up on commitments
- Maintain confidentiality

Practice Scenarios included in attachments.''',
            'order': 20,
            'is_published': True
        },
        {
            'title': 'Week 3: Financial Products Overview',
            'description': 'Comprehensive guide to banking products and services.',
            'content': '''Banking Products and Services

Understanding our product portfolio:

Deposit Products:
- Savings accounts
- Checking accounts
- Fixed deposits
- Money market accounts

Loan Products:
- Personal loans
- Home loans
- Auto loans
- Business loans

Additional Services:
- Credit cards
- Debit cards
- Online banking
- Mobile banking
- Wire transfers

Review the product comparison sheets attached.''',
            'order': 30,
            'is_published': True
        },
        {
            'title': 'Week 4: Security and Fraud Prevention',
            'description': 'Essential knowledge on protecting customer information and preventing fraud.',
            'content': '''Security and Fraud Prevention

Critical topics for protecting our customers:

1. Information Security
   - Password best practices
   - Data encryption
   - Secure document handling
   - Clean desk policy

2. Common Fraud Types
   - Identity theft
   - Phishing scams
   - Check fraud
   - Card fraud

3. Prevention Measures
   - Customer verification procedures
   - Suspicious activity monitoring
   - Reporting protocols
   - Customer education

Remember: When in doubt, always escalate to your supervisor!''',
            'order': 40,
            'is_published': True
        },
        {
            'title': 'Advanced: Risk Management',
            'description': 'For experienced staff: Understanding and managing banking risks.',
            'content': '''Risk Management in Banking

Advanced topic for senior staff:

Types of Banking Risks:
1. Credit Risk
2. Market Risk
3. Operational Risk
4. Liquidity Risk
5. Compliance Risk

Risk Management Framework:
- Identification
- Assessment
- Mitigation
- Monitoring
- Reporting

This material is supplementary for career development.''',
            'order': 100,
            'is_published': True
        },
        {
            'title': 'Reference: Banking Terminology',
            'description': 'Comprehensive glossary of banking terms and definitions.',
            'content': '''Banking Terminology Reference

Keep this handy for quick reference!

A
- APR: Annual Percentage Rate
- ATM: Automated Teller Machine
- AML: Anti-Money Laundering

B
- Balance Sheet: Financial statement showing assets and liabilities
- Beneficiary: Person who receives funds
- Branch: Physical bank location

C
- Certificate of Deposit (CD): Time deposit with fixed term
- Collateral: Asset pledged to secure a loan
- Credit Score: Numerical expression of creditworthiness

D
- Debit: Entry recording money owed
- Default: Failure to repay debt
- Deposit: Money placed in an account

...and many more in the attached glossary document!''',
            'order': 1000,
            'is_published': True
        },
        {
            'title': 'Draft: Upcoming Compliance Training',
            'description': 'New compliance requirements - under development.',
            'content': '''This lesson is being prepared and will be published soon.

Topics to be covered:
- New regulatory changes
- Updated compliance procedures
- Reporting requirements
- Training certification

Check back next week!''',
            'order': 50,
            'is_published': False  # Unpublished draft
        }
    ]
    
    created_count = 0
    
    for lesson_data in lessons_data:
        lesson, created = Lesson.objects.get_or_create(
            title=lesson_data['title'],
            defaults=lesson_data
        )
        
        if created:
            created_count += 1
            print(f"✓ Created: {lesson.title}")
        else:
            print(f"- Already exists: {lesson.title}")
    
    print(f"\n✅ Sample data creation complete!")
    print(f"📊 Created {created_count} new lesson(s)")
    print(f"📚 Total lessons in database: {Lesson.objects.count()}")
    print(f"📖 Published lessons: {Lesson.objects.filter(is_published=True).count()}")
    
    print("\n🌐 Visit http://localhost:8000 to see your lessons!")


if __name__ == '__main__':
    create_sample_lessons()
