CREATE TABLE IF NOT EXISTS login_events (
    id SERIAL PRIMARY KEY,
    raw_timestamp VARCHAR(45),
    server_hostname VARCHAR(100),
    auth_status VARCHAR(20),
    username VARCHAR(100),
    source_ip VARCHAR(45),
    source_port VARCHAR(45),
    country VARCHAR(100),
    city VARCHAR(100),
    isp VARCHAR(255),
    is_authorized_user BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS blocked_ips (
    source_ip VARCHAR(45) PRIMARY KEY,
    failed_attempts INT,
    country VARCHAR(100),
    isp VARCHAR(255),
    first_seen TIMESTAMP,
    last_seen TIMESTAMP,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
