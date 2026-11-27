/*
Created: 2026-05-25
Modified: 2026-10-06
Version: 1.10
Purpose:
- Optional beat-pulse helper for the 666 Cyber HUD.
- Run the PHASE 2 "SYSTEM ONLINE" indicator exactly once.
- Fade/blink slowly 3 times.
- Keep SYSTEM ONLINE visible after the third fade.
- Hold the final visible state for 2 seconds.
- Only then start the actual host project/system.

IMPORTANT:
There is NO automatic loop/restart of the intro or SYSTEM ONLINE sequence.
*/

(function () {
  'use strict';

  const root = document.querySelector('.lyvra-cyber-sequence');
  const logo = document.querySelector('.cyber-hud-logo');
  const systemOnline = document.querySelector('.hud-system-online');

  if (!root || !logo) return;

  /* Optional external beat pulse API. Does not affect the center emblem. */
  function pulse() {
    logo.classList.add('is-beat');
    window.setTimeout(() => logo.classList.remove('is-beat'), 130);
  }

  window.pulseCyberHudLogo = pulse;

  /* Production-safe default: no automatic demo pulse. */
  let demo = false;
  window.setCyberHudDemoPulse = function (enabled) {
    demo = !!enabled;
  };

  window.setInterval(() => {
    if (!demo) return;
    pulse();
  }, 666);

  const SYSTEM_ONLINE_ANIMATION_MS = 5400;
  const SYSTEM_ONLINE_FINAL_HOLD_MS = 2000;

  let onlineSequenceStarted = false;
  let systemStarted = false;
  let holdTimer = 0;
  let failsafeTimer = 0;

  function startHostSystem() {
    if (systemStarted) return;
    systemStarted = true;

    if (holdTimer) {
      window.clearTimeout(holdTimer);
      holdTimer = 0;
    }
    if (failsafeTimer) {
      window.clearTimeout(failsafeTimer);
      failsafeTimer = 0;
    }

    /*
      ========================================================
      HIER STARTET DAS EIGENTLICHE PROJEKT / SYSTEM.
      ========================================================

      Ablauf davor:
      1. Phase 2 wurde vollständig eingeblendet.
      2. SYSTEM ONLINE hat langsam exakt 3-mal gefadet/geblinkt.
      3. SYSTEM ONLINE blieb danach sichtbar stehen.
      4. Die sichtbare Endanzeige wurde weitere 2 Sekunden gehalten.
      5. Erst JETZT startet das eigentliche Radio / Dashboard / Projekt.

      Empfohlene Integration:
      window.addEventListener('lyvra:system-start', () => {
        // HIER: Radio / Dashboard / Projekt starten.
      });
    */

    root.classList.remove('system-online-sequence');
    root.classList.add('system-started');

    root.dispatchEvent(new CustomEvent('lyvra:system-start', { bubbles: true }));
    window.dispatchEvent(new CustomEvent('lyvra:system-start', {
      detail: { root }
    }));

    /* Optionaler direkter Host-Hook. */
    if (typeof window.startProjectSystem === 'function') {
      window.startProjectSystem();
    }
  }

  function beginFinalHold() {
    if (systemStarted) return;

    /*
      Animation endet mit opacity:1.
      SYSTEM ONLINE bleibt deshalb während dieses Holds sichtbar.
    */
    holdTimer = window.setTimeout(() => {
      startHostSystem();
    }, SYSTEM_ONLINE_FINAL_HOLD_MS);
  }

  function startSystemOnlineSequence() {
    if (onlineSequenceStarted || !systemOnline) return;
    onlineSequenceStarted = true;

    root.classList.add('system-online-sequence');

    const finishAnimation = () => {
      systemOnline.removeEventListener('animationend', finishAnimation);
      beginFinalHold();
    };

    systemOnline.addEventListener('animationend', finishAnimation, { once: true });

    /*
      Failsafe:
      Nur falls ein Browser kein animationend liefert.
      5.4 s Animation + 2 s Hold + kleine Reserve.
    */
    failsafeTimer = window.setTimeout(() => {
      failsafeTimer = 0;
      if (!systemStarted && !holdTimer) {
        beginFinalHold();
      }
    }, SYSTEM_ONLINE_ANIMATION_MS + 250);
  }

  /* Phase 2 ist nach dem Phase-1-Crossfade aktiv. */
  window.addEventListener('lyvra:intro-complete', startSystemOnlineSequence, {
    once: true
  });

  function reset() {
    if (holdTimer) window.clearTimeout(holdTimer);
    if (failsafeTimer) window.clearTimeout(failsafeTimer);
    holdTimer = 0;
    failsafeTimer = 0;
    onlineSequenceStarted = false;
    systemStarted = false;
    root.classList.remove('system-online-sequence', 'system-started');
  }

  window.addEventListener('lyvra:intro-reset', reset);

  window.LyvraCyberHud = {
    pulse,
    reset,
    startSystemOnlineSequence,
    startHostSystem
  };
})();
