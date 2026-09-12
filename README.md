# VisionInspect AI

VisionInspect AI is a manufacturing quality inspection demo with image acquisition, OpenCV anomaly detection, defect classification, severity scoring, quality decisions, inspection history, and production analytics.

## Run locally

Backend:

```powershell
Push-Location backend
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

Frontend, in a second terminal:

```powershell
Push-Location frontend
npm install
npm run dev
```

Open `http://127.0.0.1:5173/`.

Demo accounts:

- Quality engineer: `engineer@factory.com` / `password123`
- Factory supervisor: `supervisor@factory.com` / `supervisor123`
- Administrator: `admin@factory.com` / `admin12345`

## Docker

```powershell
docker compose up --build
```

The web app is available at `http://127.0.0.1:5173/` and the API documentation at `http://127.0.0.1:8000/docs`.

## API surface

- `POST /api/auth/login` authenticates demo roles.
- `POST /api/inspect` validates and inspects one image, with batch and source metadata.
- `GET /api/inspections` returns the inspection log.
- `GET /api/analytics` returns pass rate, defect mix, severity, and recent decisions.
- `GET /api/metrics` returns processing speed and automation metrics.
- `GET /api/model` returns the active model version, classes, feature count, and training sample counts.
- `GET /api/health` is the service health check.

The current persistence layer is SQLite for the milestone demo. PostgreSQL or MongoDB can replace it behind the same API contract for production deployment.

## Classification validation

Run the reproducible evaluator from `backend`:

```powershell
python evaluate_model.py
```

For a faster smoke benchmark:

```powershell
python evaluate_model.py --limit-per-class 2
```

For an unbiased validation run:

```powershell
python train_model.py
python evaluate_model.py --holdout
```

After extracting a larger MVTec archive, audit it before training:

```powershell
python dataset_audit.py
```

The evaluator reports hierarchical good/bad accuracy, bad-product precision/recall/F1, four-class accuracy, per-class metrics, and a confusion matrix. The deterministic shuffled 80/20 holdout uses 127 training images and 34 validation images. The hierarchical model reports 79.41% good/bad accuracy, 82.14% bad precision, 92.00% bad recall, and 86.79% bad F1. Four-class subtype accuracy is 52.94%, so a CNN/YOLO model with augmentation and a larger independent validation set is still recommended for production manufacturing deployment.
