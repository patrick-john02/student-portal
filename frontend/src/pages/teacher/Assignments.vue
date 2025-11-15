<script lang="ts">
export const description = "Teacher assignments listing page"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import { ref, computed } from "vue"

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

import { Plus, BookOpen, Calendar, Users } from "lucide-vue-next"

const userRole = "Teacher"

// Filters
const subjectFilter = ref("")
const sectionFilter = ref("")
const search = ref("")

// Dummy assignments
const assignments = ref([
  {
    id: 1,
    title: "Reading Comprehension Essay",
    subject: "English",
    section: "STEM 11 - A",
    due: "2025-02-15",
    submissions: 34,
    total: 40,
  },
  {
    id: 2,
    title: "Quadratic Functions Worksheet",
    subject: "Math",
    section: "HUMSS 12 - B",
    due: "2025-02-18",
    submissions: 28,
    total: 30,
  },
  {
    id: 3,
    title: "Periodic Table Activity",
    subject: "Science",
    section: "ABM 12 - A",
    due: "2025-02-20",
    submissions: 25,
    total: 28,
  },
])

const filteredAssignments = computed(() => {
  return assignments.value.filter((a) => {
    const matchSubject = subjectFilter.value ? a.subject === subjectFilter.value : true
    const matchSection = sectionFilter.value ? a.section === sectionFilter.value : true
    const matchSearch = search.value
      ? a.title.toLowerCase().includes(search.value.toLowerCase())
      : true

    return matchSubject && matchSection && matchSearch
  })
})
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
              <BreadcrumbPage>Assignments</BreadcrumbPage>
            </BreadcrumbItem>
          </BreadcrumbList>
        </Breadcrumb>
      </header>

      <!-- Page Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Title -->
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold tracking-tight">Assignments</h2>
            <p class="text-sm text-muted-foreground">
              Manage assignments, due dates, and student submissions.
            </p>
          </div>

          <Button as-child class="gap-2">
            <a href="/teacher/assignments/new">
              <Plus class="h-4 w-4" />
              New Assignment
            </a>
          </Button>
        </div>

        <!-- Summary Cards -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Total Assignments</CardTitle>
              <BookOpen class="h-5 w-5 text-blue-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">{{ assignments.length }}</p>
              <p class="text-xs text-muted-foreground mt-1">Across all classes</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Upcoming Deadlines</CardTitle>
              <Calendar class="h-5 w-5 text-green-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">3</p>
              <p class="text-xs text-muted-foreground mt-1">Within the week</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Submissions</CardTitle>
              <Users class="h-5 w-5 text-purple-500" />
            </CardHeader>
            <CardContent>
              <p class="text-2xl font-bold">87%</p>
              <p class="text-xs text-muted-foreground mt-1">Submission rate</p>
            </CardContent>
          </Card>
        </div>

        <!-- Filters -->
        <Card>
          <CardHeader>
            <CardTitle>Filters</CardTitle>
            <CardDescription>Sort assignments by subject, section, or name</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              <!-- Subject -->
              <Select v-model="subjectFilter">
                <SelectTrigger class="w-full">
                  <SelectValue placeholder="Select Subject" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="Math">Math</SelectItem>
                  <SelectItem value="English">English</SelectItem>
                  <SelectItem value="Science">Science</SelectItem>
                </SelectContent>
              </Select>

              <!-- Section -->
              <Select v-model="sectionFilter">
                <SelectTrigger class="w-full">
                  <SelectValue placeholder="Select Section" />
                </SelectTrigger>
                <SelectContent>
                  <SelectItem value="STEM 11 - A">STEM 11 - A</SelectItem>
                  <SelectItem value="ABM 12 - A">ABM 12 - A</SelectItem>
                  <SelectItem value="HUMSS 12 - B">HUMSS 12 - B</SelectItem>
                </SelectContent>
              </Select>

              <!-- Search -->
              <Input v-model="search" placeholder="Search assignment..." />
            </div>
          </CardContent>
        </Card>

        <!-- Table -->
        <Card>
          <CardHeader>
            <CardTitle>Assignments</CardTitle>
            <CardDescription>List of all assignments created</CardDescription>
          </CardHeader>

          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Title</TableHead>
                  <TableHead>Subject</TableHead>
                  <TableHead>Section</TableHead>
                  <TableHead class="text-center">Due</TableHead>
                  <TableHead class="text-center">Submissions</TableHead>
                </TableRow>
              </TableHeader>

              <TableBody>
                <TableRow
                  v-for="a in filteredAssignments"
                  :key="a.id"
                  class="hover:bg-muted/50 cursor-pointer"
                  @click="$router.push(`/teacher/assignments/${a.id}`)"
                >
                  <TableCell class="font-medium">
                    {{ a.title }}
                  </TableCell>

                  <TableCell>
                    <Badge variant="secondary">{{ a.subject }}</Badge>
                  </TableCell>

                  <TableCell>{{ a.section }}</TableCell>

                  <TableCell class="text-center">
                    {{ a.due }}
                  </TableCell>

                  <TableCell class="text-center font-semibold">
                    {{ a.submissions }}/{{ a.total }}
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
