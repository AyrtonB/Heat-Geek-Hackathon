

export const SCOP_INTERVAL = 0.1
export const MIN_SCOP = 2.8
export const MAX_SCOP = 5.0
export const SCOP_VALUES: number[] = []
for(let i = MIN_SCOP; i <= MAX_SCOP; i += SCOP_INTERVAL) {
    SCOP_VALUES.push(i)
}