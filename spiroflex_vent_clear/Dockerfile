FROM golang:1.24-alpine AS builder

WORKDIR /src
COPY source/go.mod source/go.sum ./
RUN go mod download
COPY source/ ./

ARG TARGETARCH
RUN CGO_ENABLED=0 GOOS=linux GOARCH=${TARGETARCH} \
    go build -trimpath -ldflags="-s -w" -o /ventclear ./cmd/ventclear

FROM ghcr.io/home-assistant/base:3.24

ARG BUILD_VERSION

LABEL \
  io.hass.version="${BUILD_VERSION}" \
  io.hass.type="app" \
  org.opencontainers.image.title="Spiroflex ecoVENT Simple" \
  org.opencontainers.image.source="https://github.com/xmemphis-xyz/homeassistant-addon-spiroflex-vent-clear"

COPY --from=builder /ventclear /usr/bin/ventclear

RUN printf '%s\n' \
    '#!/usr/bin/with-contenv bashio' \
    '' \
    'if [ ! -f /data/options.json ]; then' \
    '  bashio::log.error "Home Assistant app configuration is missing."' \
    '  exit 1' \
    'fi' \
    '' \
    'export SPIROFLEX_CONFIG_FILE="/data/options.json"' \
    '' \
    'bashio::log.info "Starting Spiroflex ecoVENT Simple REST bridge"' \
    'exec /usr/bin/ventclear' \
    > /run.sh \
    && chmod +x /run.sh

CMD ["/run.sh"]
