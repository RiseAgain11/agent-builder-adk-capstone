from mcp.server.fastmcp import FastMCP

mcp = FastMCP("medical_exam_server")


@mcp.tool()
def get_exam_info(exam_name: str) -> dict:
    """Return official information sources for NEET, MCAT, or UCAT."""

    exams = {
        "NEET": {
            "country": "India",
            "purpose": "Medical entrance exam for undergraduate medical admission.",
            "official_sources": ["https://nta.ac.in/", "https://neet.nta.nic.in/"],
        },
        "MCAT": {
            "country": "United States and Canada",
            "purpose": "Medical College Admission Test for medical school admissions.",
            "official_sources": ["https://students-residents.aamc.org/mcat"],
        },
        "UCAT": {
            "country": "UK, Australia, New Zealand",
            "purpose": "Admissions test used by many medical and dental schools.",
            "official_sources": ["https://www.ucat.ac.uk/"],
        },
    }

    key = exam_name.strip().upper()

    if key not in exams:
        return {
            "status": "not_found",
            "message": "Available exams: NEET, MCAT, UCAT",
        }

    return {
        "status": "found",
        "exam": key,
        "data": exams[key],
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
