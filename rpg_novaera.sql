USE rpg_novaera;

-- Jogadores
CREATE TABLE jogadores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tipo_raca VARCHAR(50), -- humanos, organismos_cyber, micro_inteligentes, monstros
    planeta_inicial_id INT,
    creditos DECIMAL(10,2) DEFAULT 0, -- moeda do jogo
    pontos INT DEFAULT 0,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Universos
CREATE TABLE universos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    tamanho INT,
    velocidade_tick INT, -- tempo entre ticks em segundos
    duracao_ticks INT, -- duração do jogo em ticks
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Setores
CREATE TABLE setores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    universo_id INT,
    nome VARCHAR(100),
    FOREIGN KEY (universo_id) REFERENCES universos(id)
);

-- Galáxias
CREATE TABLE galaxias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    setor_id INT,
    nome VARCHAR(100),
    FOREIGN KEY (setor_id) REFERENCES setores(id)
);

-- Sistemas Solares
CREATE TABLE sistemas_solares (
    id INT AUTO_INCREMENT PRIMARY KEY,
    galaxia_id INT,
    nome VARCHAR(100),
    FOREIGN KEY (galaxia_id) REFERENCES galaxias(id)
);

-- Planetas
CREATE TABLE planetas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sistema_id INT,
    nome VARCHAR(100),
    owner_id INT NULL, -- jogador dono
    owner_type ENUM('player', 'bot', 'neutral') DEFAULT 'neutral',
    recurso_metal INT DEFAULT 0,
    recurso_cristal INT DEFAULT 0,
    recurso_combustivel INT DEFAULT 0,
    recurso_energia INT DEFAULT 0,
    FOREIGN KEY (sistema_id) REFERENCES sistemas_solares(id),
    FOREIGN KEY (owner_id) REFERENCES jogadores(id)
);

-- Estruturas Planetárias
CREATE TABLE estruturas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    planeta_id INT,
    tipo VARCHAR(100), -- mina_metal, mina_cristal, sintetizador_combustivel, planta_solar, laboratorio, hangar, silo
    nivel INT DEFAULT 1,
    FOREIGN KEY (planeta_id) REFERENCES planetas(id)
);

-- Frotas
CREATE TABLE frotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jogador_id INT,
    planeta_origem_id INT,
    planeta_destino_id INT NULL,
    tipo_nave VARCHAR(50), -- caca, corveta, fragata, destroyer, cruzador, nave_mae, sonda, coletora, extratora, colonizadora
    quantidade INT DEFAULT 1,
    tempo_viagem_ticks INT DEFAULT 0,
    FOREIGN KEY (jogador_id) REFERENCES jogadores(id),
    FOREIGN KEY (planeta_origem_id) REFERENCES planetas(id),
    FOREIGN KEY (planeta_destino_id) REFERENCES planetas(id)
);

-- Logs por Tick
CREATE TABLE logs_tick (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tick_id INT,
    jogador_id INT,
    acao VARCHAR(255),
    detalhes TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (jogador_id) REFERENCES jogadores(id)
);

-- Eventos Cósmicos
CREATE TABLE eventos_cosmicos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    universo_id INT,
    tick_acontecimento INT,
    tipo_evento VARCHAR(100), -- chuva_meteoros, cometa, supernova, etc.
    descricao TEXT,
    FOREIGN KEY (universo_id) REFERENCES universos(id)
);

-- Combates
CREATE TABLE combates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    atacante_id INT,
    defensor_id INT,
    planeta_id INT,
    resultado VARCHAR(50), -- vitória_atacante, vitória_defensor, empate
    recursos_capturados TEXT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (atacante_id) REFERENCES jogadores(id),
    FOREIGN KEY (defensor_id) REFERENCES jogadores(id),
    FOREIGN KEY (planeta_id) REFERENCES planetas(id)
);

-- Expedições
CREATE TABLE expedicoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jogador_id INT,
    planeta_origem_id INT,
    destino_descricao VARCHAR(255),
    resultado TEXT,
    tempo_ticks INT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (jogador_id) REFERENCES jogadores(id),
    FOREIGN KEY (planeta_origem_id) REFERENCES planetas(id)
);

-- Pontuações
CREATE TABLE pontuacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jogador_id INT,
    pontos INT,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (jogador_id) REFERENCES jogadores(id)
);
