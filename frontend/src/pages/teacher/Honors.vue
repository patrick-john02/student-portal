<script lang="ts">
export const description = "Teacher honors listing page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref } from "vue"

import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  SidebarProvider,
  SidebarInset,
  SidebarTrigger,
} from "@/components/ui/sidebar"

import {
  Breadcrumb,
  BreadcrumbList,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"

import { Separator } from "@/components/ui/separator"

import {
  Card,
  CardHeader,
  CardTitle,
  CardDescription,
  CardContent,
} from "@/components/ui/card"

import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { Input } from "@/components/ui/input"
import { Select, SelectTrigger, SelectContent, SelectItem, SelectValue } from "@/components/ui/select"

import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table"

import { Crown, Medal, Users, Star } from "lucide-vue-next"

const userRole = "Teacher"

const gradeFilter = ref("")
const sectionFilter = ref("")
const search = ref("")

// Dummy honors data
const honors = ref([
  {
    id: 1,
    name: "Samantha Cruz",
    section: "STEM 11 - A",
    gradeLevel: "Grade 11",
    gpa: 96.4,
    rank: 1,
  },
  {
    id: 2,
    name: "Elijah Montes",
    section: "STEM 11 - A",
    gradeLevel: "Grade 11",
    gpa: 94.2,
    rank: 2,
  },
  {
    id: 3,
    name: "Marjorie Tan",
    section: "HUMSS 12 - B",
    gradeLevel: "Grade 12",
    gpa: 95.1,
    rank: 1,
  },
  {
    id: 4,
    name: "Joshua Ramirez",
    section: "ABM 12 - A",
    gradeLevel: "Grade 12",
    gpa: 93.8,
    rank: 2,
  },
])
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 px-4">
        <SidebarTrigger class="-ml-1" />
        <Separator orientation="vertical" class="mx-2 h-4" />

        <Breadcrumb>
          <BreadcrumbList>
            <BreadcrumbItem>
              <BreadcrumbLink href="/teacher/dashboard">Teacher</BreadcrumbLink>
            </BreadcrumbItem>
            <BreadcrumbSeparator />
            <BreadcrumbItem>
              <BreadcrumbPage>Honors</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Honors</h2>
            <p class="text-sm text-muted-foreground">
              View honor students, rankings, and performance summaries.
            </p>
          </div>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Top Honors</CardTitle>
              <Crown class="h-5 w-5 text-yellow-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">8</p>
              <p class="text-xs text-muted-foreground mt-1">Across all sections</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">With Honors</CardTitle>
              <Medal class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">21</p>
              <p class="text-xs text-muted-foreground mt-1">Consistent achievers</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Honors %</CardTitle>
              <Star class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">14%</p>
              <p class="text-xs text-muted-foreground mt-1">Overall performance</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Students</CardTitle>
              <Users class="h-5 w-5 text-purple-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">212</p>
              <p class="text-xs text-muted-foreground mt-1">Enrolled this year</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>Sort honors by grade and section</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Grade Level -->
              <Select v-model="gradeFilter">
                <SelectTrigger class="w-full">
                  <SelectValue placeholder="Select Grade Level" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Grade 11">Grade 11</SelectItem>
                  <SelectItem value="Grade 12">Grade 12</SelectItem>
                </SelectContent>
              </Select>

              <!-- Section -->
              <Select v-model="sectionFilter">
                <SelectTrigger class="w-full">
                  <SelectValue placeholder="Select Section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search student..." />
            </div>
          </CardContent>
        </Card>

        <!-- Honors Table -->
        <Card>
          <CardHeader>
            <CardTitle>Honor Students</CardTitle>
            <CardDescription>Ranked by general weighted average (GWA)</CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead class="w-12 text-center">Rank</TableHead>
                  <TableHead>Name</TableHead>
                  <TableHead>Grade Level</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead class="text-center">GWA</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="h in honors"
                  :key="h.id"
                  class="hover:bg-muted/50 cursor-pointer"
                >
                  <TableCell class="text-center font-bold">
                    {{ h.rank }}
                  </TableCell>

                  <TableCell class="font-medium">
                    {{ h.name }}
                  </TableCell>

                  <TableCell>
                    <Badge variant="secondary">{{ h.gradeLevel }}</Badge>
                  </TableCell>

                  <TableCell>{{ h.section }}</TableCell>

                  <TableCell class="text-center font-semibold">
                    {{ h.gpa }}%
                  </TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
