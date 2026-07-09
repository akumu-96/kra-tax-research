import pandas as pd
from datetime import datetime
from typing import List, Dict, Optional
import random
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF  # For generating research papers

# ======================
# 1. Research Paper Generation
# ======================
class ResearchPaper:
    def __init__(self, title: str, author: str, topic: str):
        self.title = title
        self.author = author
        self.topic = topic  # e.g., Tax Policy, Revenue Performance, Compliance
        self.sections: List[Dict] = []
        self.references: List[str] = []
        self.status = "Draft"  # Draft, Under Review, Published

    def add_section(self, section_title: str, content: str):
        self.sections.append({
            "title": section_title,
            "content": content,
            "word_count": len(content.split())
        })
        return {"status": "Added", "section": section_title}

    def add_reference(self, reference: str):
        self.references.append(reference)
        return {"status": "Added", "reference": reference}

    def generate_paper(self, filename: str = "research_paper.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, txt=self.title, ln=1, align="C")
        pdf.cell(200, 10, txt=f"By: {self.author}", ln=2, align="C")
        pdf.cell(200, 10, txt=f"Topic: {self.topic}", ln=2, align="C")
        pdf.ln(10)

        # Sections
        for section in self.sections:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=section["title"], ln=1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=section["content"])
            pdf.ln(5)

        # References
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="References", ln=1)
        pdf.set_font("Arial", size=12)
        for ref in self.references:
            pdf.cell(200, 10, txt=ref, ln=1)

        pdf.output(filename)
        self.status = "Published"
        return {"status": "Generated", "filename": filename}

# ======================
# 2. Sectoral Analysis
# ======================
class SectoralAnalysis:
    def __init__(self, sector: str):
        self.sector = sector  # e.g., Construction, Manufacturing
        self.revenue_data: List[Dict] = []
        self.performance_metrics: Dict = {}
        self.region = "East Africa"

    def add_revenue_data(self, year: int, revenue: float, growth_rate: float):
        self.revenue_data.append({
            "year": year,
            "revenue": revenue,
            "growth_rate": growth_rate
        })
        return {"status": "Added", "year": year, "revenue": revenue}

    def analyze_performance(self):
        if not self.revenue_data:
            return {"status": "No Data"}

        total_revenue = sum(data["revenue"] for data in self.revenue_data)
        avg_growth = np.mean([data["growth_rate"] for data in self.revenue_data])
        latest_year = max(data["year"] for data in self.revenue_data)
        latest_revenue = next(data["revenue"] for data in self.revenue_data if data["year"] == latest_year)

        self.performance_metrics = {
            "total_revenue": total_revenue,
            "avg_growth_rate": avg_growth,
            "latest_year": latest_year,
            "latest_revenue": latest_revenue,
            "sector": self.sector,
            "region": self.region
        }
        return self.performance_metrics

    def visualize_trends(self):
        if not self.revenue_data:
            return {"status": "No Data"}

        years = [data["year"] for data in self.revenue_data]
        revenues = [data["revenue"] for data in self.revenue_data]

        plt.figure(figsize=(10, 6))
        plt.plot(years, revenues, marker="o", label="Revenue")
        plt.title(f"{self.sector} Sector Revenue Trend in {self.region}")
        plt.xlabel("Year")
        plt.ylabel("Revenue (KES)")
        plt.grid(True)
        plt.legend()
        plt.savefig(f"{self.sector}_revenue_trend.png")
        plt.close()
        return {"status": "Visualized", "file": f"{self.sector}_revenue_trend.png"}

# ======================
# 3. Tax Analysis (iTax Simulation)
# ======================
class TaxAnalysis:
    def __init__(self):
        self.tax_returns: List[Dict] = []
        self.ledger: List[Dict] = []
        self.compliance_status = "Compliant"

    def file_return(self, taxpayer_id: str, tax_type: str, amount: float, date: str):
        return_id = f"RET-{random.randint(1000, 9999)}"
        self.tax_returns.append({
            "return_id": return_id,
            "taxpayer_id": taxpayer_id,
            "tax_type": tax_type,  # e.g., VAT, Income Tax, Withholding Tax
            "amount": amount,
            "date": date,
            "status": "Filed"
        })
        return {"status": "Filed", "return_id": return_id}

    def confirm_payment(self, return_id: str, payment_amount: float, payment_date: str):
        for tax_return in self.tax_returns:
            if tax_return["return_id"] == return_id:
                tax_return["payment_status"] = "Confirmed"
                tax_return["payment_amount"] = payment_amount
                tax_return["payment_date"] = payment_date
                self.ledger.append({
                    "return_id": return_id,
                    "amount": payment_amount,
                    "date": payment_date,
                    "type": "Payment"
                })
                return {"status": "Confirmed", "return_id": return_id, "amount": payment_amount}
        return {"status": "Failed", "message": "Return not found"}

    def update_ledger(self, transaction: Dict):
        self.ledger.append(transaction)
        return {"status": "Updated", "transaction": transaction}

    def validate_vat_slips(self, slips: List[Dict], bank_statements: List[Dict]):
        validated = []
        discrepancies = []

        for slip in slips:
            slip_found = False
            for statement in bank_statements:
                if (slip["amount"] == statement["amount"] and
                    slip["date"] == statement["date"] and
                    slip["taxpayer_id"] == statement["taxpayer_id"]):
                    validated.append(slip)
                    slip_found = True
                    break
            if not slip_found:
                discrepancies.append(slip)

        if discrepancies:
            self.compliance_status = "Non-Compliant"
            return {"status": "Discrepancies Found", "validated": validated, "discrepancies": discrepancies}
        else:
            self.compliance_status = "Compliant"
            return {"status": "All Validated", "validated": validated}

# ======================
# 4. Technical Committee Report
# ======================
class TechnicalCommitteeReport:
    def __init__(self, title: str, committee: str, date: str):
        self.title = title
        self.committee = committee
        self.date = date
        self.sections: List[Dict] = []
        self.recommendations: List[str] = []

    def add_section(self, title: str, content: str):
        self.sections.append({
            "title": title,
            "content": content
        })
        return {"status": "Added", "section": title}

    def add_recommendation(self, recommendation: str):
        self.recommendations.append(recommendation)
        return {"status": "Added", "recommendation": recommendation}

    def generate_report(self, filename: str = "technical_report.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Title
        pdf.cell(200, 10, txt=self.title, ln=1, align="C")
        pdf.cell(200, 10, txt=f"Committee: {self.committee}", ln=2, align="C")
        pdf.cell(200, 10, txt=f"Date: {self.date}", ln=2, align="C")
        pdf.ln(10)

        # Sections
        for section in self.sections:
            pdf.set_font("Arial", "B", 12)
            pdf.cell(200, 10, txt=section["title"], ln=1)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, txt=section["content"])
            pdf.ln(5)

        # Recommendations
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="Recommendations", ln=1)
        pdf.set_font("Arial", size=12)
        for rec in self.recommendations:
            pdf.cell(200, 10, txt=f"• {rec}", ln=1)

        pdf.output(filename)
        return {"status": "Generated", "filename": filename}

# ======================
# Example Usage
# ======================
if __name__ == "__main__":
    # --- Research Paper ---
    paper = ResearchPaper(
        title="Tax Policy Reforms in East Africa: A Sectoral Analysis",
        author="Your Name",
        topic="Tax Policy"
    )
    paper.add_section(
        "Introduction",
        "This paper examines the impact of recent tax policy reforms on revenue performance in East Africa..."
    )
    paper.add_section(
        "Methodology",
        "Data was collected from the Kenya Revenue Authority's iTax system and analyzed using Python..."
    )
    paper.add_reference("Kenya Revenue Authority (2023). Annual Report.")
    paper.add_reference("East African Community (2022). Tax Harmonization Policy.")
    paper.generate_paper("tax_policy_research.pdf")
    print("\n--- Research Paper Generated ---")

    # --- Sectoral Analysis ---
    construction_analysis = SectoralAnalysis("Construction")
    construction_analysis.add_revenue_data(2020, 500000000, 0.05)
    construction_analysis.add_revenue_data(2021, 550000000, 0.10)
    construction_analysis.add_revenue_data(2022, 600000000, 0.09)
    construction_analysis.add_revenue_data(2023, 650000000, 0.08)
    performance = construction_analysis.analyze_performance()
    construction_analysis.visualize_trends()
    print("\n--- Construction Sector Analysis ---")
    print(performance)

    manufacturing_analysis = SectoralAnalysis("Manufacturing")
    manufacturing_analysis.add_revenue_data(2020, 800000000, 0.03)
    manufacturing_analysis.add_revenue_data(2021, 850000000, 0.06)
    manufacturing_analysis.add_revenue_data(2022, 900000000, 0.06)
    manufacturing_analysis.add_revenue_data(2023, 950000000, 0.05)
    manufacturing_performance = manufacturing_analysis.analyze_performance()
    manufacturing_analysis.visualize_trends()
    print("\n--- Manufacturing Sector Analysis ---")
    print(manufacturing_performance)

    # --- Tax Analysis ---
    tax_analyst = TaxAnalysis()
    tax_analyst.file_return("TP001", "VAT", 500000.0, "2024-06-01")
    tax_analyst.file_return("TP002", "Income Tax", 1000000.0, "2024-06-05")
    tax_analyst.confirm_payment("RET-1234", 500000.0, "2024-06-02")
    tax_analyst.update_ledger({"transaction_id": "T001", "amount": 500000.0, "date": "2024-06-02", "type": "VAT Payment"})

    # VAT Slip Validation
    vat_slips = [
        {"slip_id": "SL001", "amount": 500000.0, "date": "2024-06-02", "taxpayer_id": "TP001"},
        {"slip_id": "SL002", "amount": 250000.0, "date": "2024-06-03", "taxpayer_id": "TP002"}
    ]
    bank_statements = [
        {"statement_id": "BS001", "amount": 500000.0, "date": "2024-06-02", "taxpayer_id": "TP001"},
        {"statement_id": "BS002", "amount": 250000.0, "date": "2024-06-03", "taxpayer_id": "TP002"}
    ]
    validation_result = tax_analyst.validate_vat_slips(vat_slips, bank_statements)
    print("\n--- VAT Slip Validation ---")
    print(validation_result)
    print(f"Compliance Status: {tax_analyst.compliance_status}")

    # --- Technical Committee Report ---
    report = TechnicalCommitteeReport(
        title="Sectoral Revenue Performance Report",
        committee="Technical Committee on Revenue Analysis",
        date="2024-06-30"
    )
    report.add_section(
        "Construction Sector",
        "The construction sector showed a steady growth of 8-10% annually..."
    )
    report.add_section(
        "Manufacturing Sector",
        "Manufacturing revenue grew by 5-6% annually, with challenges in..."
    )
    report.add_recommendation("Implement targeted audits for high-risk sectors.")
    report.add_recommendation("Enhance iTax system integration for real-time monitoring.")
    report.generate_report("sectoral_analysis_report.pdf")
    print("\n--- Technical Committee Report Generated ---")
