mei2vexflowTables = {};
mei2vexflowTables.positions = {
    above: Vex.Flow.Modifier.Position.ABOVE,
    below: Vex.Flow.Modifier.Position.BELOW
};
mei2vexflowTables.hairpins = {
    cres: Vex.Flow.StaveHairpin.type.CRESC,
    dim: Vex.Flow.StaveHairpin.DESCRESC
};
mei2vexflowTables.articulations = {
    acc: "a>",
    stacc: "a.",
    ten: "a-",
    stacciss: "av",
    marc: "a^",
    dnbow: "am",
    upbow: "a|",
    snap: "ao",
    lhpizz: "a+",
    dot: "a.",
    stroke: "a|"
};
mei2vexflowTables.barlines = {
    rptstart: Vex.Flow.Barline.type.REPEAT_BEGIN,
    rptend: Vex.Flow.Barline.type.REPEAT_END,
    end: Vex.Flow.Barline.type.END
};
Node.prototype.attrs = function () {
    var b;
    var a = {};
    for (b in this.attributes) {
        a[this.attributes[b].name] = this.attributes[b].value;
    }
    return a;
};
Array.prototype.all = function (b) {
    b = b || function (c) {
        return c === true;
    };
    var a;
    for (a = 0; a < this.length; a++) {
        if (b(this[a]) === false) {
            return false;
        }
    }
    return true;
};
Array.prototype.any = function (b) {
    b = b || function (c) {
        return c === true;
    };
    var a;
    for (a = 0; a < this.length; a++) {
        if (b(this[a]) === true) {
            return true;
        }
    }
    return false;
};
var render_notation = function (d, a, b, e) {
    b = b || 800;
    e = e || 350;
    var F, p, Q;
    var D = [];
    var c = [];
    var E = [];
    var M = [];
    var H;
    $("mei\\:score").hide();
    var y = function (S) {
        S = (typeof S === "number" && arguments.length === 2 && typeof arguments[1] === "object") ? arguments[1] : S;
        return $(S).attr("pname") + "/" + $(S).attr("oct");
    };
    var K = function (S) {
        var U = $(S).find("mei\\:syl");
        var T = "";
        $(U).each(function (W, X) {
            var Y = ($(X).attr("wordpos") == "i" || $(X).attr("wordpos") == "m") ? "-" : "";
            T += (W > 0 ? "\n" : "") + $(X).text() + Y;
        });
        var V = (U.attr("wordpos") == "i" || U.attr("wordpos") == "m") ? "-" : "";
        return T;
    };
    var t = function (W, T) {
        var U = $(W).find("mei\\:dir");
        var S = "";
        var V = "";
        $(U).each(function () {
            if ($(this).attr("startid") == $(T).attr("xml:id")) {
                S += $(this).text().trim();
                V = $(this).attr("place");
            }
        });
        return [S, V];
    };
    var m = function (W, S) {
        var U = $(W).find("mei\\:dynam");
        var T = "";
        var V = "";
        $(U).each(function () {
            if ($(this).attr("startid") == $(S).attr("xml:id")) {
                T += $(this).text().trim();
                V = $(this).attr("place");
            }
        });
        return [T, V];
    };
    var l = function (T, S) {
        T = {
            pitch: T.split("/")[0][0],
            octave: Number(T.split("/")[1])
        };
        S = {
            pitch: S.split("/")[0][0],
            octave: Number(S.split("/")[1])
        };
        if (T.octave === S.octave) {
            if (T.pitch === S.pitch) {
                return 0;
            } else {
                if (T.pitch < S.pitch) {
                    return -1;
                } else {
                    if (T.pitch > S.pitch) {
                        return 1;
                    }
                }
            }
        } else {
            if (T.octave < S.octave) {
                return -1;
            } else {
                if (T.octave > S.octave) {
                    return 1;
                }
            }
        }
    };
    var v = function (T, S) {};
    var q = function (S) {
        S = String(S);
        if (S === "breve") {
            return "d";
        }
        if (S === "1") {
            return "w";
        }
        if (S === "2") {
            return "h";
        }
        if (S === "4") {
            return "q";
        }
        if (S === "8") {
            return "8";
        }
        if (S === "16") {
            return "16";
        }
        if (S === "32") {
            return "32";
        }
        if (S === "64") {
            return "64";
        }
        throw new Vex.RuntimeError("BadArguments", 'The MEI duration "' + S + '" is not supported.');
    };
    var h = function (S, U) {
        U = U || true;
        S = (typeof S === "number" && arguments.length === 2 && typeof arguments[1] === "object") ? arguments[1] : S;
        if ($(S).attr("dur") === undefined) {
            alert("Could not get duration from:\n" + JSON.stringify(S, null, "\t"));
        }
        var T = q($(S).attr("dur"));
        if (U === true && $(S).attr("dots") === "1") {
            T += "d";
        }
        return T;
    };
    var C = function (S) {
        if (S === "n") {
            return "n";
        }
        if (S === "f") {
            return "b";
        }
        if (S === "s") {
            return "#";
        }
        if (S === "ff") {
            return "bb";
        }
        if (S === "ss") {
            return "##";
        }
        return undefined;
    };
    var s = function (S) {
        var T = $(S).attr("accid");
        if (T !== undefined) {
            return C($(S).attr("accid"));
        }
    };
    var f = function (T, S) {
        var U = $(T).attr("stem.dir");
        if (U !== undefined) {
            return (U === "up") ? Vex.Flow.StaveNote.STEM_UP : (U === "down") ? Vex.Flow.StaveNote.STEM_DOWN : undefined;
        } else {
            var V = N($(S).attr("n"));
            if (V === "treble") {
                return (l("a/5", y(T)) == 1) ? Vex.Flow.StaveNote.STEM_UP : Vex.Flow.StaveNote.STEM_DOWN;
            } else {
                if (V === "bass") {
                    return (l("c/4", y(T)) == -1) ? Vex.Flow.StaveNote.STEM_UP : Vex.Flow.StaveNote.STEM_DOWN;
                }
            }
        }
    };
    var g = function (S) {
        if ($(S).attr("key.pname") !== undefined && $(S).attr("key.mode") !== undefined) {
            var T = $(S).attr("key.pname").toUpperCase();
            if ($(S).attr("key.accid") !== undefined) {
                if ($(S).attr("key.accid") === "s") {
                    T += "#";
                } else {
                    if ($(S).attr("key.accid") === "f") {
                        T += "b";
                    }
                }
            }
            T += $(S).attr("key.mode") === "major" ? "" : "m";
            return T;
        }
    };
    var w = function (S) {
        if ($(S).attr("clef.shape") === "G" && $(S).attr("clef.trans") === "8vb") {
            return "octave";
        } else {
            if ($(S).attr("clef.shape") === "G") {
                return "treble";
            } else {
                if ($(S).attr("clef.shape") === "F") {
                    return "bass";
                } else {
                    if ($(S).attr("clef.shape") === "C" && $(S).attr("clef.line") === "3") {
                        return "alto";
                    } else {
                        if ($(S).attr("clef.shape") === "C" && $(S).attr("clef.line") === "1") {
                            return "soprano";
                        }
                    }
                }
            }
        }
    };
    var N = function (S) {
        var T = $(d).find("mei\\:staffdef[n=" + S + "]")[0];
        return w(T);
    };
    var k = function (S) {
        if ($(S).attr("meter.count") !== undefined && $(S).attr("meter.unit") !== undefined) {
            return $(S).attr("meter.count") + "/" + $(S).attr("meter.unit");
        }
    };
    var A = function (S) {
        F = new Vex.Flow.Renderer(S, Vex.Flow.Renderer.Backends.CANVAS);
        Q = F.getContext();
    };
    var R = function (X, aa, W, Y, ac, V, ab, T, S, ae, Z, U) {
        var ad = new Vex.Flow.Stave(V, ab, T);
        if (W === true) {
            ad.addClef(w(aa));
        }
        if (Y === true) {
            if ($(aa).attr("key.sig.show") === "true" || $(aa).attr("key.sig.show") === undefined) {
                ad.addKeySignature(g(aa));
            }
        }
        if (ac === true) {
            if ($(aa).attr("meter.rend") === "norm" || $(aa).attr("meter.rend") === undefined) {
                ad.addTimeSignature(k(aa));
            }
        }
        if (S !== false) {
            ad.setBegBarType(mei2vexflowTables.barlines[S]);
        }
        if (ae !== false) {
            console.log(ad.setEndBarType(mei2vexflowTables.barlines[ae]));
            ad.setEndBarType(mei2vexflowTables.barlines[ae]);
        }
        if (Z !== false) {
            ad.setVoltaType(Z[1], Z[0] + ".", 28);
        }
        if (U !== false) {
            ad.setMeasure(U);
        }
        ad.setContext(Q).draw();
        return ad;
    };
    var I = function () {
        H = "staff-wise";
        $(d).find("mei\\:staffdef").each(function (Y, Z) {
            D[(Number($(Z).attr("n")))] = R(Y, Z, true, true, true, 0, Y * 100, b, false, false, false, false);
        });
        var W;
        for (var staff_n in D) {
            var X = $(d).find("mei\\:staff[n=" + staff_n + "]").map(z).get();
            var U = {};
            for (W = 0; W < X.length; W++) {
                var T = X[W].layer;
                if (U.hasOwnProperty(T)) {
                    U[T].push.apply(U[T], X[W].events);
                } else {
                    U[T] = X[W].events;
                }
            }
            var S = [];
            for (var T in U) {
                S.push(x(null, U[T]));
            }
            var V = new Vex.Flow.Formatter().joinVoices(S).format(S, b);
            $.each(S, function (Y, Z) {
                Z.draw(Q, D[staff_n]);
            });
            $.each(E, function (Z, Y) {
                Y.setContext(Q).draw();
            });
        }
    };
    var P = function () {
        H = "measure-wise";
        $(d).find("mei\\:measure").each(u);
        $.each(E, function (T, S) {
            S.setContext(Q).draw();
        });
        $(d).find("mei\\:tie").each(G);
        $(d).find("mei\\:slur").each(G);
        $(d).find("mei\\:hairpin").each(O);
    };
    var G = function (S, T) {
        f_note = null;
        l_note = null;
        $(M).each(function (U, V) {
            if (V.id == $(T).attr("startid")) {
                f_note = V.vexNote;
            } else {
                if (V.id == $(T).attr("endid")) {
                    l_note = V.vexNote;
                }
            }
        });
        new Vex.Flow.StaveTie({
            first_note: f_note,
            last_note: l_note,
            first_indices: [0],
            last_indices: [0]
        }).setContext(Q).draw();
    };
    var O = function (S, T) {
        f_note = null;
        l_note = null;
        $(M).each(function (U, V) {
            if (V.id == $(T).attr("startid")) {
                f_note = V.vexNote;
            }
            if (V.id == $(T).attr("endid")) {
                l_note = V.vexNote;
            }
        });
        place = mei2vexflowTables.positions[$(T).attr("place")];
        type = mei2vexflowTables.hairpins[$(T).attr("form")];
        l_ho = 0;
        r_ho = 0;
        dur_ticks = (parseFloat($(T).attr("dur")) * Vex.Flow.RESOLUTION) / (parseFloat($($.find("mei\\:staffdef")[0]).attr("meter.count")) + 1);
        hairpin_options = {
            height: 10,
            y_shift: 0,
            left_shift_px: l_ho,
            r_shift_px: r_ho
        };
        new Vex.Flow.StaveHairpin({
            first_note: f_note,
            last_note: l_note,
        }, type).setContext(Q).setRenderOptions(hairpin_options).setPosition(place).draw();
    };
    var u = function (S, T) {
        if (H === "staff-wise") {
            return $(T).find("mei\\:staff").map(function (V, U) {
                return z(V, U, T);
            }).get();
        } else {
            if (H === "measure-wise") {
                c.push($(T).find("mei\\:staff").map(function (V, U) {
                    return z(V, U, T);
                }).get());
            }
        }
    };
    var z = function (ag, aj, Y) {
        if (H === "staff-wise") {
            return $(aj).find("mei\\:layer").map(function (am, al) {
                return r(am, al, aj, Y);
            }).get();
        } else {
            if (H === "measure-wise") {
                var ai = $(d).find("mei\\:measure").get().length;
                var W = $(Y).prevAll("mei\\:measure").length === 0;
                var S = $(Y).nextAll("mei\\:measure").length === 0;
                var aa = Math.round(b / ai);
                var ah = $(Y).attr("n");
                var ab = $(Y).attr("left") !== undefined ? $(Y).attr("left") : false;
                var ak = $(Y).attr("right") !== undefined ? $(Y).attr("right") : false;
                var ad = $(Y).parent("mei\\:ending").length > 0 && $(aj)[0] === $(Y).find("mei\\:staff")[0] ? [$(Y).parent().attr("n").substring(0, 1), W ? Vex.Flow.Volta.type.BEGIN : S ? Vex.Flow.Volta.type.END : Vex.Flow.Volta.type.MID] : false;
                var ac, T, ae;
                if (Y === $(d).find("mei\\:measure")[0]) {
                    T = 0;
                    ae = (Number(aj.attrs().n) - 1) * 100;
                    staffdef = $(d).find("mei\\:staffdef[n=" + aj.attrs().n + "]")[0];
                    ac = R(null, staffdef, true, true, true, T, ae, aa + 30, ab, ak, ad, false);
                } else {
                    var U = c[c.length - 1][0];
                    T = U.x + U.width;
                    ae = (Number(aj.attrs().n) - 1) * 100;
                    if ($(Y).prevAll().length > 0 && $(Y).prevAll("mei\\:measure").length === 0) {
                        scoredef = $(Y).prevAll("mei\\:scoredef:first").get(0);
                        ac = R(null, scoredef, false, false, $(scoredef).attr("meter.count") ? true : false, T, ae, aa + 30, ab, ak, ad, false);
                    } else {
                        ac = R(null, $(d).find("mei\\:staffdef[n=" + aj.attrs().n + "]")[0], false, false, false, T, ae, aa, ab, ak, ad, false);
                    }
                }
                var V = $(aj).find("mei\\:layer").map(function (am, al) {
                    return r(am, al, aj, Y);
                }).get();
                var Z = [];
                $(V).each(function () {
                    Z.push({
                        events: $(this.events).get().map(function (al) {
                            return al.vexNote ? al.vexNote : al;
                        }),
                        layer: this.layer
                    });
                });
                var X = $.map(Z, function (al) {
                    return x(null, al.events);
                });
                var af = new Vex.Flow.Formatter().joinVoices(X).format(X, aa).formatToStave(X, ac);
                $.each(X, function (al, am) {
                    am.draw(Q, ac);
                });
                return ac;
            }
        }
    };
    var r = function (U, T, S, V) {
        return {
            layer: U,
            events: $(T).children().map(function (X, W) {
                return B(X, W, T, S, V);
            }).get()
        };
    };
    var L = function (V, S, Z, W) {
        function X(ad) {
            return (new Vex.Flow.Annotation(ad)).setFont("Times").setBottom(true);
        }

        function U(ad) {
            return (new Vex.Flow.Annotation(ad)).setFont("Times");
        }
        try {
            var aa = new Vex.Flow.StaveNote({
                keys: [y(V)],
                clef: N($(Z).attr("n")),
                duration: h(V),
                stem_direction: f(V, Z)
            });
            aa.addAnnotation(0, X(K(V)));
            var T = t(W, V);
            aa.addAnnotation(0, T[1] == "below" ? X(T[0]) : U(T[0]));
            var ac = m(W, V);
            aa.addAnnotation(0, ac[1] == "below" ? X(ac[0]) : U(ac[0]));
            try {
                for (i = 0; i < parseInt($(V).attr("dots"), 10); i++) {
                    aa.addDotToAll();
                }
            } catch (ab) {
                throw new Vex.RuntimeError("BadArguments", "A problem occurred processing the dots of <mei:note>: " + JSON.stringify(V.attrs()) + '. "' + ab.message + '"');
            }
            if ($(V).attr("accid")) {
                aa.addAccidental(0, new Vex.Flow.Accidental(s(V)));
            }
            $.each($(V).find("mei\\:artic"), function (ae, ad) {
                aa.addArticulation(0, new Vex.Flow.Articulation(mei2vexflowTables.articulations[$(ad).attr("artic")]).setPosition(mei2vexflowTables.positions[$(ad).attr("place")]));
            });
            $.each($(V).children(), function (ad, ae) {
                $(ae).remove();
            });
            if (!$(V).attr("xml:id")) {
                throw new Vex.RuntimeError("BadArguments", "mei:note must have a xml:id attribute.");
            }
            var Y = {
                vexNote: aa,
                id: $(V).attr("xml:id")
            };
            M.push(Y);
            return Y;
        } catch (ab) {
            throw new Vex.RuntimeError("BadArguments", "A problem occurred processing the <mei:note>: " + JSON.stringify(V.attrs()) + '. "' + ab.message + '"');
        }
    };
    var J = function (W, S, Z, X) {
        function Y(ac) {
            return (new Vex.Flow.Annotation(ac)).setFont("Times").setBottom(true);
        }

        function V(ac) {
            return (new Vex.Flow.Annotation(ac)).setFont("Times");
        }
        try {
            var U = new Vex.Flow.StaveNote({
                keys: ["c/5"],
                duration: h(W, false) + "r"
            });
            var T = t(X, W);
            U.addAnnotation(2, T[1] == "below" ? Y(T[0]) : V(T[0]));
            var ab = m(X, W);
            U.addAnnotation(2, ab[1] == "below" ? Y(ab[0]) : V(ab[0]));
            if ($(W).attr("dots") === "1") {
                note.addDotToAll();
            }
            return U;
        } catch (aa) {
            throw new Vex.RuntimeError("BadArguments", "A problem occurred processing the <mei:rest>: " + JSON.stringify(W.attrs()) + '. "' + aa.message + '"');
        }
    };
    var n = function (U, S, X, V) {
        function W(ab) {
            return (new Vex.Flow.Annotation(ab)).setFont("Times").setBottom(true);
        }

        function T(ab) {
            return (new Vex.Flow.Annotation(ab)).setFont("Times");
        }
        try {
            var Y = new Vex.Flow.StaveNote({
                keys: ["c/5"],
                duration: "wr"
            });
            annot = t(V, U);
            Y.addAnnotation(2, annot[1] == "below" ? W(annot[0]) : T(annot[0]));
            var aa = m(V, U);
            Y.addAnnotation(2, aa[1] == "below" ? W(aa[0]) : T(aa[0]));
            return Y;
        } catch (Z) {
            throw new Vex.RuntimeError("BadArguments", "A problem occurred processing the <mei:mRest>: " + JSON.stringify(U.attrs()) + '. "' + Z.message + '"');
        }
    };
    var o = function (U, T, S, W) {
        var V = $(U).children().map(function (X, Y) {
            var Z = B(X, Y, T, S, W);
            return Z.vexNote ? Z.vexNote : Z;
        }).get();
        E.push(new Vex.Flow.Beam(V));
        return V;
    };
    var j = function (V, S, Y, X) {
        try {
            var aa = $(V).children().map(y).get();
            var T = q(Math.max.apply(Math, $(V).children().map(function () {
                return Number($(this).attr("dur"));
            }).get()));
            var W = $(V).children().map(function () {
                return $(this).attr("dots") === "1";
            }).get().any();
            if (W === true) {
                T += "d";
            }
            var U = new Vex.Flow.StaveNote({
                keys: aa,
                clef: N($(Y).attr("n")),
                duration: T
            });
            if (W === true) {
                U.addDotToAll();
            }
            $(V).children().each(function (ab, ac) {
                if ($(ac).attr("accid") !== undefined) {
                    U.addAccidental(ab, new Vex.Flow.Accidental(s(ac)));
                }
            });
            return U;
        } catch (Z) {
            throw new Vex.RuntimeError("BadArguments", "A problem occurred processing the <mei:chord>: " + JSON.stringify($.each($(V).children(), function (ac, ab) {
                ab.attrs();
            }).get()) + '. "' + Z.message + '"');
        }
    };
    var B = function (V, U, T, S, X) {
        var W = $(U).get(0).tagName.toLowerCase();
        if (W === "mei:rest") {
            return J(U, T, S, X);
        } else {
            if (W === "mei:mrest") {
                return n(U, T, S, X);
            } else {
                if (W === "mei:note") {
                    return L(U, T, S, X);
                } else {
                    if (W === "mei:beam") {
                        return o(U, T, S, X);
                    } else {
                        if (W === "mei:chord") {
                            return j(U, T, S, X);
                        } else {
                            throw new Vex.RuntimeError("BadArguments", 'Rendering of element "' + W + '" is not supported.');
                        }
                    }
                }
            }
        }
    };
    var x = function (T, S) {
        if (!$.isArray(S)) {
            throw new Vex.RuntimeError("BadArguments", "make_voice() voice_contents argument must be an array.");
        }
        var U = new Vex.Flow.Voice({
            num_beats: Number($(d).find("mei\\:staffdef").attr("meter.count")),
            beat_value: Number($(d).find("mei\\:staffdef").attr("meter.unit")),
            resolution: Vex.Flow.RESOLUTION
        });
        U.setStrict(false);
        U.addTickables(S);
        return U;
    };
    A(a);
    P();
};