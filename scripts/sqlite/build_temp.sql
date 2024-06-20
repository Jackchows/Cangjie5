DROP TABLE IF EXISTS build_temp;
CREATE TABLE "build_temp" (
	"unicode_hex" TEXT NULL,
	"character_value" TEXT NULL,
	"code_value" TEXT NULL,
	"marks" TEXT NULL,
	"block" TEXT NULL,
	"block_no" INTEGER NULL,
	"is_letter" INTEGER NULL,
	"repeat_order" INTEGER NULL,
	"repeat_code" TEXT NULL,
	"unicode_dec" INTEGER NULL,
	"id" INTEGER PRIMARY KEY autoincrement
);
CREATE INDEX idx_build_temp_code_value on build_temp(code_value);
CREATE INDEX idx_build_temp_repeat_order on build_temp(repeat_order);
CREATE INDEX idx_build_temp_repeat_code on build_temp(repeat_code);
