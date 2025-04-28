USE rpg_novaera;

CREATE PROCEDURE process_tick()
BEGIN
    UPDATE planetas
    SET 
        recurso_metal = recurso_metal + 10,
        recurso_cristal = recurso_cristal + 5,
        recurso_combustivel = recurso_combustivel + 3,
        recurso_energia = recurso_energia + 7;

    INSERT INTO logs_tick (tick_id, jogador_id, acao, detalhes)
    SELECT 0, owner_id, 'Produção', CONCAT('Recursos produzidos no planeta ', nome)
    FROM planetas WHERE owner_id IS NOT NULL;
END
