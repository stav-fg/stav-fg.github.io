// Run with the Figma tool (use_figma) on "Portfolio 26". Use the filled-in copy that
// tools/figma_text_sync.py prepare writes to private/figma-sync/figma_check.js.
// Returns, per page, the Figma lines that are not on the site, and the numbers of the site lines that
// are not in Figma. The hash and the clean-up of spaces match tools/figma_text_sync.py exactly.
const FRAMES = /*FRAMES*/null;
const SITE = /*SITE*/null;
const norm = s => s.replace(/\s+/g, ' ').trim();
const fnv = s => { let h = 0x811c9dc5; for (let i = 0; i < s.length; i++) { h ^= s.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; } return h.toString(16).padStart(8, '0'); };
const visible = n => { for (let p = n; p && p.type !== 'PAGE'; p = p.parent) { if (!p.visible) return false; } return true; };
const inPicture = t => { for (let p = t.parent; p && p.type !== 'PAGE'; p = p.parent) { if (/^Chart |^Illustration|^Device|^Lock illustration/.test(p.name)) return true; } return false; };
const result = {};
for (const [page, id] of Object.entries(FRAMES)) {
  const frame = await figma.getNodeByIdAsync(id);
  if (!frame) { result[page] = { error: 'frame ' + id + ' not found' }; continue; }
  const lines = [];
  frame.findAll(t => t.type === 'TEXT' && visible(t) && !inPicture(t)).forEach(t => t.characters.split('\n').forEach(l => { const s = norm(l); if (s) lines.push(s); }));
  const figHashes = new Set(lines.map(fnv));
  const site = SITE[page];
  const siteAll = new Set([...site.b, ...site.x]);
  const fresh = [...new Set(lines.filter(l => !siteAll.has(fnv(l))))];
  const missing = site.b.map((h, i) => figHashes.has(h) ? -1 : i).filter(i => i >= 0);
  result[page] = { frame: frame.name, new: fresh, missing };
}
return result;
