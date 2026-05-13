# Dental Clinic Management (Odoo 17)

<p align="center">
  <img src="dental_clinic/static/description/icon.png" width="128" alt="Dental Clinic logo"/>
</p>

A complete dental clinic management module for **Odoo 17 Community / Enterprise**.

## Features

- 🧑‍⚕️ **Patient files** with medical history, allergies, chronic diseases, current medications, emergency contact
- 👩‍⚕️ **Practitioners / Dentists** with specialities, license numbers, color-coded calendars
- 🪑 **Rooms / Dental chairs** management
- 📅 **Appointments** with calendar (week / month / day), conflict detection, status workflow (Draft → Confirmed → Checked-In → Done / No-Show / Cancelled), email reminders
- 🦷 **Interactive Odontogram** — 32 teeth automatically created per patient with FDI numbering; track condition (healthy, caries, filling, crown, root canal, extracted, implant, bridge…) and affected surface (occlusal / mesial / distal / buccal / lingual)
- 🧾 **Treatment catalog** linked to product/service for invoicing
- 📋 **Treatment plans** with line-by-line tooth-specific procedures, quantities, prices, discounts, totals
- 💊 **Prescriptions** with medication lines (dosage / frequency / duration / instructions) and printable PDF
- 💰 **Billing**: one-click invoice creation from a treatment plan (uses native `account.move` — **no insurance**)
- 🔒 **Security**: three groups — Receptionist / Dentist (User) / Manager — with proper access rights and record rules
- 📨 **Email templates** for appointment reminders
- 🖨️ **PDF reports**: Patient Card, Treatment Plan, Prescription
- 🧪 **Demo data** included to test instantly

## Repository layout

```
dental/
├── README.md
└── dental_clinic/            ← the Odoo module (technical name)
    ├── __manifest__.py
    ├── __init__.py
    ├── models/
    ├── views/
    ├── security/
    ├── data/
    ├── demo/
    ├── report/
    ├── wizards/
    └── static/
        ├── description/
        │   ├── icon.png
        │   └── index.html
        └── src/css/odontogram.css
```

## Installation

1. Clone the repository in your Odoo addons folder:
   ```bash
   cd /path/to/odoo/custom_addons
   git clone https://github.com/souhaibouadi/dental.git
   ```

2. Make sure that folder is listed in `addons_path` (in `odoo.conf`):
   ```ini
   addons_path = /path/to/odoo/addons, /path/to/odoo/custom_addons
   ```

3. Restart Odoo and update the apps list:
   ```bash
   ./odoo-bin -c odoo.conf -u base -d your_database
   ```

4. In Odoo: **Apps** → remove the "Apps" filter → search **"Dental Clinic Management"** → click **Install**.

5. (Optional) To see demo data, create a fresh database with "Load demonstration data" enabled.

## Usage

After installation a new top menu **"Dental"** appears with this structure:

| Menu | Sub-menu | Action |
|------|----------|--------|
| Dashboard | — | Calendar of appointments (landing) |
| Patients | All Patients / Odontogram | Patient kanban, list, form; full odontogram |
| Appointments | Calendar / All Appointments / Today | Schedule and follow-up |
| Clinical | Treatment Plans / Prescriptions | Build plans, write Rx |
| Billing | Patient Invoices | All out-invoices linked to a patient |
| Configuration | Treatment Catalog / Practitioners / Rooms | Master data |

### Typical workflow

1. **Receptionist** creates a patient (auto-creates the odontogram + a contact).
2. **Receptionist** books an appointment in the Calendar — overlap is prevented.
3. **Dentist** opens the patient → builds a **Treatment Plan**, adds lines (tooth + treatment + price) → confirms.
4. **Dentist** clicks **Create Invoice** to bill it. Odoo native invoice is created.
5. **Dentist** writes a **Prescription** and clicks **Print** → PDF.

### Security groups

| Group | Capabilities |
|-------|-------------|
| Receptionist | Create / view patients & appointments. Read-only on practitioners & treatments. |
| Dentist (User) | Full clinical access: medical records, plans, prescriptions, odontogram. |
| Manager | Full access + configuration (treatments, rooms, practitioners). |

Assign users via *Settings → Users & Companies → Users → Dental Clinic*.

## Dependencies

`base`, `mail`, `contacts`, `product`, `account`, `calendar` — all part of standard Odoo 17.

## Compatibility

- Odoo **17.0** (Community & Enterprise)

## License

LGPL-3.0

## Author

[@souhaibouadi](https://github.com/souhaibouadi)

---

# Gestion de Clinique Dentaire (Odoo 17) — FR

Module complet de gestion d'une clinique dentaire pour **Odoo 17**.

## Fonctionnalités

- 🧑‍⚕️ **Fiches patients** : antécédents médicaux, allergies, maladies chroniques, traitements en cours, contact d'urgence
- 👩‍⚕️ **Praticiens** : spécialités, n° de licence, couleurs au calendrier
- 🪑 **Salles / Fauteuils** dentaires
- 📅 **Rendez-vous** avec vue calendrier, détection de conflits, workflow complet, rappels par email
- 🦷 **Odontogramme** — 32 dents générées automatiquement par patient (notation FDI)
- 🧾 **Catalogue de soins** lié à un produit/service pour la facturation
- 📋 **Plans de traitement** détaillés (dent par dent, quantité, prix, remise)
- 💊 **Ordonnances** avec PDF imprimable
- 💰 **Facturation** : création de facture en un clic depuis un plan de traitement (`account.move` natif — **pas d'assurance**)
- 🔒 **Sécurité** en 3 groupes : Réceptionniste / Dentiste / Manager
- 🖨️ **Rapports PDF** : fiche patient, plan de traitement, ordonnance
- 🧪 **Données de démonstration** incluses

## Installation rapide

```bash
cd /path/to/odoo/custom_addons
git clone https://github.com/souhaibouadi/dental.git
```

Puis dans Odoo : **Apps → Mettre à jour la liste → "Dental Clinic Management" → Installer**.

Un nouveau menu *Dental* apparaît avec : Tableau de bord, Patients, Rendez-vous, Clinique, Facturation, Configuration.

## Licence

LGPL-3.0
