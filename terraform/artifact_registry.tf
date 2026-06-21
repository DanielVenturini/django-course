resource "google_artifact_registry_repository" "django_app" {
  location      = var.region
  repository_id = var.artifact_registry_repository_name
  format        = "DOCKER"

  docker_config {
    immutable_tags = false
  }
}