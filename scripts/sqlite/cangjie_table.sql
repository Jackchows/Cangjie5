DROP TABLE IF EXISTS cangjie_table;
CREATE TABLE IF NOT EXISTS cangjie_table 
(unicode_hex     TEXT,
 character_value TEXT,
 code_value      TEXT,
 marks           TEXT,
 "block"           TEXT,
 block_no        INTEGER,
 is_letter       INTEGER,
 selected         INTEGER,
 unicode_dec     INTEGER,
 "id"             INTEGER);
CREATE UNIQUE INDEX idx_cangjie_table_id on cangjie_table("id");
CREATE INDEX idx_cangjie_table_unicode_hex on cangjie_table(unicode_hex);
CREATE INDEX idx_cangjie_table_block on cangjie_table("block");
CREATE INDEX idx_cangjie_table_block_id on cangjie_table(block_no);
CREATE INDEX idx_cangjie_table_selected on cangjie_table(selected);