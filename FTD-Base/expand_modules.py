#!/usr/bin/env python3
"""
Script to expand FTD modules with premium content sections
"""

# Module expansions data - tailored content for each module
EXPANSIONS = {
    "modulo-2-2.html": {
        "title": "Arquitetura de Aplicações com IA",
        "color": "tecnico",
        "sections": [
            {
                "type": "projects",
                "title": "3 Arquiteturas de Produção",
                "projects": [
                    {
                        "name": "Microserviços com IA",
                        "stack": "Docker + Kubernetes + FastAPI + Redis + RabbitMQ",
                        "desc": "Arquitetura escalável com serviços independentes para NLP, embeddings e inference",
                        "features": ["Service mesh pattern", "Load balancing inteligente", "Auto-scaling baseado em latência", "Circuit breaker por serviço"]
                    },
                    {
                        "name": "Serverless AI Pipeline",
                        "stack": "AWS Lambda + Step Functions + S3 + DynamoDB",
                        "desc": "Pipeline event-driven para processamento de documentos em massa",
                        "features": ["Pay-per-use (90% mais barato)", "Auto-scaling infinito", "Retry logic automático", "Dead letter queues"]
                    },
                    {
                        "name": "Edge AI com Caching Inteligente",
                        "stack": "Cloudflare Workers + KV + Durable Objects",
                        "desc": "IA distribuída globalmente com latência <50ms",
                        "features": ["Deploy em 200+ datacenters", "Semantic caching global", "Geo-routing automático", "Cost < $100/mês para 1M requests"]
                    }
                ]
            }
        ]
    },
    "modulo-2-3.html": {
        "title": "RAG e Knowledge Bases",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-4.html": {
        "title": "Fine-tuning e Customização",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-5.html": {
        "title": "Agentes e Workflows Complexos",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-6.html": {
        "title": "Monitoramento e Observabilidade",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-7.html": {
        "title": "Testing e QA em IA",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-8.html": {
        "title": "Deploy e MLOps",
        "color": "tecnico",
        "sections": []
    },
    "modulo-2-9.html": {
        "title": "Ética e Governança",
        "color": "tecnico",
        "sections": []
    }
}

# This script is just for planning - actual expansion will be done manually
# to ensure premium quality for each module
if __name__ == "__main__":
    print(f"Total modules to expand: {len(EXPANSIONS)}")
    for module, data in EXPANSIONS.items():
        print(f"  - {module}: {data['title']}")
