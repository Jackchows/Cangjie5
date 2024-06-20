DROP TABLE IF EXISTS unicode_point;
CREATE TABLE unicode_point
(
    "unicode_hex" TEXT NOT NULL,
    "character_value" TEXT NULL,
    "block" TEXT NOT NULL,
    "point" TEXT NOT NULL
);

INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0x3007', '〇', 'SP', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa0e', '﨎', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa0f', '﨏', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa11', '﨑', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa13', '﨓', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa14', '﨔', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa1f', '﨟', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa21', '﨡', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa23', '﨣', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa24', '﨤', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa27', '﨧', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa28', '﨨', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0xfa29', '﨩', 'CI', 'U');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0x303e', '〾', 'SP', 'IDC');
INSERT INTO unicode_point (unicode_hex, character_value, block, point) VALUES ('0x31ef', '㇯', 'S', 'IDC');
COMMIT;
