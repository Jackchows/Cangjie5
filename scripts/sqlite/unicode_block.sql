DROP TABLE IF EXISTS "unicode_block";
CREATE TABLE IF NOT EXISTS "unicode_block" (
    name            TEXT,
    name_abbr       TEXT,
    start_hex       TEXT,
    end_hex         TEXT,
    start_dec       INTEGER,
    end_dec         INTEGER,
    area_no         INTEGER
);

INSERT INTO "unicode_block" ("name", "name_abbr", "start_hex", "end_hex", "start_dec", "end_dec", "area_no") VALUES
	('CJK Unified Ideographs', 'U', '0x4e00', '0x9fff', 19968, 40959, 1),
	('CJK Unified Ideographs Extension A', 'UA', '0x3400', '0x4dbf', 13312, 19903, 2),
	('CJK Unified Ideographs Extension B', 'UB', '0x20000', '0x2a6df', 131072, 173791, 3),
	('CJK Unified Ideographs Extension C', 'UC', '0x2a700', '0x2b739', 173824, 177977, 4),
	('CJK Unified Ideographs Extension D', 'UD', '0x2b740', '0x2b81d', 177984, 178205, 5),
	('CJK Unified Ideographs Extension E', 'UE', '0x2b820', '0x2cea1', 178208, 183969, 6),
	('CJK Unified Ideographs Extension F', 'UF', '0x2ceb0', '0x2ebe0', 183984, 191456, 7),
	('CJK Unified Ideographs Extension G', 'UG', '0x30000', '0x3134a', 196608, 201546, 8),
	('CJK Unified Ideographs Extension H', 'UH', '0x31350', '0x323af', 201552, 205743, 9),
	('CJK Unified Ideographs Extension I', 'UI', '0x2ebf0', '0x2ee5d', 191472, 192093, 10),
	('CJK Compatibility Ideographs', 'CI', '0xf900', '0xfaff', 63744, 64255, 11),
	('CJK Compatibility Ideographs Supplement', 'CIS', '0x2f800', '0x2fa1f', 194560, 195103, 12),
	('Kangxi Radicals', 'KR', '0x2f00', '0x2fdf', 12032, 12255, 13),
	('CJK Radicals Supplement', 'RS', '0x2e80', '0x2eff', 11904, 12031, 14),
	('CJK Strokes', 'S', '0x31c0', '0x31e3', 12736, 12771, 15),
	('CJK Symbols and Punctuation', 'SP', '0x3000', '0x303f', 12288, 12351, 16),
	('CJK Compatibility Forms', 'CF', '0xfe30', '0xfe4f', 65072, 65103, 17),
	('Bopomofo', 'B', '0x3100', '0x312f', 12544, 12591, 18),
	('Ideographic Description Character', 'IDC', '0x2ff0', '0x2fff', 12272, 12287, 19),
	('Counting Rod Numerals', 'CRN', '0x1d360', '0x1d37f', 119648, 119679, 20),
	('Private Use Area', 'PUA', '0xe000', '0xf8ff', 57344, 63743, 97),
	('Supplementary Private Use Area-A', 'PUAA', '0xf0000', '0xffffd', 983040, 1048573, 98),
	('Supplementary Private Use Area-B', 'PUAB', '0x100000', '0x10fffd', 1048576, 1114109, 99);
COMMIT;