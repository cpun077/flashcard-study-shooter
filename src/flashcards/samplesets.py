import json

def sampleSet(num) :
    if (num == 0) :
        return basicset

    if (num == 1) :
        return recycleset

basicset = [
    {"t": "term1", "d": "def1"},
    {"t": "term2", "d": "def2"},
    {"t": "term3", "d": "def3"},
    {"t": "term4", "d": "def4"},
]
recycleset = [
    {"t": "Alkaine batteries", "d": "if possible, recycle, or do as your local laws require."},
    {"t": "Button batteries", "d": "hazardous waste. contain mercuric oxides, lithium, silver oxide, or zincair. return to manufacturer, recycle, or do as your local authorities require."},
    {"t": "lithium and lithium ion batteries", "d": "non-hazardous and recycleable"},
    {"t": "nickel-cadmium (NiCad) batteries", "d": "hazardous waste. Take to household waste site or recycling site"},
    {"t": "nickel metal hydride (NiMH) batteries", "d": "non-hazardous waste in most states (not cali) and recycleable"},
    {"t": "CRT moniters", "d": "contain many toxins and caustic substances that are illegal to incinerate . Contact local authorities for recycling and discharge before disposal."},
    {"t": "PC Systems", "d": "Recycle, give away, or resell them. Some PC contain $5-$20 in precious metals. Clean hard drive before disposing."},
    {"t": "Power Supply", "d": "Discharge before disposal. Contact local authorities & recycle if possible."},
    {"t": "Laser Printer Toner Cartridges", "d": "return to manufacture for recycling. Use toner vacuum (never a regular vacuum) or a damp cloth and scoop to clean up spills."},
    {"t": "Inkjet Printer Cartridges", "d": "Recycle them yourself or return them to the manufacturer."},
    {"t": "Cleaning solutions and solvents", "d": "consult MSDS, licensed disposal agency, or local authorities for proper disposal procedures."}
]

_all_ = sampleSet